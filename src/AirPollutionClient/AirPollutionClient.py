from datetime import datetime
from enum import IntEnum
from src.GenericClient.Client import Client, parse_response
from src.GeocodingClient import GeocodingApiClient
from src._utils import UnixTime


class AirPollutionUrls(IntEnum):
    current = 0
    forecast = 1
    historical = 2


def unix_time_to_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def response_dt_to_date(response):
    for item in response['list']:
        if timestamp := item.get('dt'):
            item['dt'] = unix_time_to_date(timestamp)
    return response


def process_response(response):
    dict_response = parse_response(response)
    dict_response['timezone'] = 'UTC'
    dict_response = response_dt_to_date(dict_response)
    return dict_response


class AirPollutionClient(Client):
    API_URLS = [
        "https://api.openweathermap.org/data/2.5/air_pollution",
        "https://api.openweathermap.org/data/2.5/air_pollution/forecast",
        "http://api.openweathermap.org/data/2.5/air_pollution/history"
    ]

    def __init__(self, api_key):
        super().__init__(api_key)
        self._cache = {}
        self._geocoding_client = GeocodingApiClient(api_key)

    def current_air_pollution_by_city_name(self, city_name: str, country_code=None, state_code=None, **kwargs):
        lat, lon = self._get_coordinates(city_name, country_code, state_code)

        self._get_params_dict = {
            "lat": lat,
            "lon": lon
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._get_request(
            self.API_URLS[AirPollutionUrls.current]
        )
        response = process_response(request_response)
        return response

    def forecast_air_pollution(self, city_name: str, country_code=None, state_code=None, **kwargs):
        lat, lon = self._get_coordinates(city_name, country_code, state_code)
        self._get_params_dict = {
            "lat": lat,
            "lon": lon
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._get_request(
            self.API_URLS[AirPollutionUrls.forecast]
        )
        response = process_response(request_response)
        return response

    def historical_air_pollution(self, city_name: str, *, start: UnixTime, end: UnixTime, country_code=None, state_code=None, **kwargs):
        lat, lon = self._get_coordinates(city_name, country_code, state_code)
        self._get_params_dict = {
            "lat": lat,
            "lon": lon,
            "start": str(start),
            "end": str(end)
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._get_request(
            self.API_URLS[AirPollutionUrls.forecast]
        )
        response = process_response(request_response)
        return response

    def _get_coordinates(self, city_name: str, country_code=None, state_code=None):
        SINGLE_LOCATION = 0
        if not (coordinates := self._cache.get((city_name, country_code, state_code))):
            coordinates = (self._geocoding_client.get_coordinates_by_location_name(city_name, country_code, state_code))[SINGLE_LOCATION]
            self._cache[(city_name, country_code, state_code)] = coordinates

        return coordinates["lat"], coordinates["lon"]


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
    client = AirPollutionClient(api_key)
    response = client.current_air_pollution_by_city_name(
        'Sosnowiec',
        'PL',
    )
    print(response)
    response = client.forecast_air_pollution(
        'Sosnowiec',
        'PL',
    )
    print(response)
    response = client.historical_air_pollution(
        'Sosnowiec',
        start=start,
        end=end
    )
    print(response)
