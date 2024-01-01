from src.AirPollutionClient._utils import AirPollutionUrls, process_air_polution_response
from src.GenericClient.base_client import Client
from src.GeocodingClient.GeocodingClient import GeocodingApiClient
from src.util.UnixTime import UnixTime


class AirPollutionClient(Client):
    _API_URLS = [
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

        _get_params_dict = {
            "lat": lat,
            "lon": lon
        }
        self._add_optional_params_from_kwargs_to_request_params(_get_params_dict, kwargs)
        request_response = self._request(
            'GET',
            self._API_URLS[AirPollutionUrls.current],
            _get_params_dict
        )
        response = process_air_polution_response(request_response)
        return response

    def forecast_air_pollution(self, city_name: str, country_code=None, state_code=None, **kwargs):
        lat, lon = self._get_coordinates(city_name, country_code, state_code)
        _get_params_dict = {
            "lat": lat,
            "lon": lon
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._request(
            'GET',
            self._API_URLS[AirPollutionUrls.forecast],
            _get_params_dict
        )
        response = process_air_polution_response(request_response)
        return response

    def historical_air_pollution(self, city_name: str, *, start: UnixTime, end: UnixTime, country_code=None, state_code=None, **kwargs):
        lat, lon = self._get_coordinates(city_name, country_code, state_code)
        _get_params_dict = {
            "lat": lat,
            "lon": lon,
            "start": str(start),
            "end": str(end)
        }
        self._add_optional_params_from_kwargs_to_request_params(_get_params_dict, kwargs)
        request_response = self._request(
            'GET',
            self._API_URLS[AirPollutionUrls.forecast],
            _get_params_dict
        )
        response = process_air_polution_response(request_response)
        return response

    def _get_coordinates(self, city_name: str, country_code=None, state_code=None):
        SINGLE_LOCATION = 0
        if not (coordinates := self._cache.get((city_name, country_code, state_code))):
            coordinates = (self._geocoding_client.get_coordinates_by_location_name(city_name, country_code, state_code))[SINGLE_LOCATION]
            self._cache[(city_name, country_code, state_code)] = coordinates

        return coordinates["lat"], coordinates["lon"]






