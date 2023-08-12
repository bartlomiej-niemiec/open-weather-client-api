from datetime import datetime
import requests
from src.GenericClient.Client import Client
from src.GeocodingClient import GeocodingApiClient
from src._utils import UnixTime

_CURR_AIR_POLLUTION = "https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
_FORECAST_AIR_POLLUTION = "https://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}"
_HISTORICAL_AIR_POLLUTION = "http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={api_key}"


class AirPollutionClient(Client):

    def __init__(self, api_key):
        super().__init__(api_key)
        self._cache = {}
        self._geocoding_client = GeocodingApiClient(api_key)

    def unix_time_to_date(self, timestamp):
        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def _response_dt_to_date(self, response):
        for item in response['list']:
            if timestamp := item.get('dt'):
                item['dt'] = self.unix_time_to_date(timestamp)
        return response

    def _process_response(self, response):
        dict_response = self._parse_response(response)
        dict_response['timezone'] = 'UTC'
        dict_response = self._response_dt_to_date(dict_response)
        return dict_response

    def current_air_pollution(self, city: str, country: str):
        if not (coordinates := self._cache.get((city, country))):
            coordinates = self._geocoding_client.get_coordinates(city, country)
            self._cache[(city, country)] = coordinates
        http_request = _CURR_AIR_POLLUTION.format(
            lat=coordinates['lat'],
            lon=coordinates['lon'],
            api_key=self.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for current weather"
        response = self._process_response(response)
        return response

    def forecast_air_pollution(self, city: str, country: str):
        if not (coordinates := self._cache.get((city, country))):
            coordinates = self._geocoding_client.get_coordinates(city, country)
            self._cache[(city, country)] = coordinates
        http_request = _FORECAST_AIR_POLLUTION.format(
            lat=coordinates['lat'],
            lon=coordinates['lon'],
            api_key=self.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for current weather"
        response = self._process_response(response)
        return response

    def historical_air_pollution(self, city: str, country: str, start: UnixTime, end: UnixTime):
        if not (coordinates := self._cache.get((city, country))):
            coordinates = self._geocoding_client.get_coordinates(city, country)
            self._cache[(city, country)] = coordinates
        http_request = _HISTORICAL_AIR_POLLUTION.format(
            lat=coordinates['lat'],
            lon=coordinates['lon'],
            start=str(start),
            end=str(end),
            api_key=self.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for current weather"
        response = self._process_response(response)
        return response


if __name__ == "__main__":
    api_key = "API_KEY"
    end_time = datetime.now()
    end = UnixTime(
        year=end_time.year,
        month=end_time.month,
        day=end_time.day,
        hour=end_time.hour,
        minutes=end_time.minute,
    )
    start = UnixTime(
        year=2023,
        month=8,
        day=2,
    )
    response = AirPollutionClient(api_key).current_air_pollution(
        'Sosnowiec',
        'PL',
    )
