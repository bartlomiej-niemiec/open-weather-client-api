import requests
from src.GeocodingClient import GeocodingApiClient
from _open_weather import OpenWeatherRequest


class AirPollutionClient(GeocodingApiClient):

    def __init__(self, api_key):
        super().__init__(api_key)
        self.cache = {}

    def current_air_pollution(self, city: str, country: str, **kwargs):
        if not (coordinates := self.cache.get((city, country))):
            coordinates = self.get_coordinates(city, country)
            self.cache[(city, country)] = coordinates
        http_request = OpenWeatherRequest.CURR_AIR_POLLUTION.format(
            lat=coordinates['lat'],
            lon=coordinates['lon'],
            api_key=self.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for current weather"
        return self._parse_response(response)

    def forecast_air_pollution(self, city: str, country: str, **kwargs):
        if not (coordinates := self.cache.get((city, country))):
            coordinates = self.get_coordinates(city, country)
            self.cache[(city, country)] = coordinates
        http_request = OpenWeatherRequest.FORECAST_AIR_POLLUTION.format(
            lat=coordinates['lat'],
            lon=coordinates['lon'],
            api_key=self.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for current weather"
        return self._parse_response(response)

    def historical_air_pollution(self, city: str, country: str, start: str, end: str):
        #TO DO


if __name__ == "__main__":
    api_key = "API_KEY"
    response = AirPollutionClient(api_key).forecast_air_pollution(
        'Sosnowiec',
        'PL'
    )
