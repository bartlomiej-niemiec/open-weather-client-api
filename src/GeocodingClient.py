from enum import IntEnum
from typing import Any
from src.GenericClient.Client import Client, parse_response


class GeocodingUrls(IntEnum):
    by_location_name = 0
    by_zip_code = 1
    reverse = 2


class GeocodingApiClient(Client):
    ALLOWED_OPTIONAL_PARS = ['limit']
    API_URLS = [
        "https://api.openweathermap.org/geo/1.0/direct",
        "http://api.openweathermap.org/geo/1.0/zip",
        "http://api.openweathermap.org/geo/1.0/reverse"
    ]

    def get_coordinates_by_location_name(self, city_name: str, country_code: str=None, state_code=None, **kwargs) -> dict[str, Any]:
        _get_params_dict = {
            "q": (city_name, state_code, country_code)
        }
        self._add_optional_params_from_kwargs_to_request_params(_get_params_dict, kwargs)
        request_response = self._get_request(
            self.API_URLS[GeocodingUrls.by_location_name],
            _get_params_dict
        )
        response = parse_response(request_response)
        return response

    def get_coordinates_by_zip_code(self, zip_code: str, country_code: str, **kwargs) -> dict[str, Any]:
        _get_params_dict = {
            "zip": (zip_code, country_code)
        }
        self._add_optional_params_from_kwargs_to_request_params(_get_params_dict, kwargs)
        request_response = self._get_request(
            self.API_URLS[GeocodingUrls.by_zip_code],
            _get_params_dict
        )
        response = parse_response(request_response)
        return response

    def get_name_of_location_by_coordiantes(self, latitude, longitude, **kwargs) -> list:
        _get_params_dict = {
            "lat": latitude,
            "lon": longitude
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._get_request(
            self.API_URLS[GeocodingUrls.reverse],
            _get_params_dict
        )
        response = parse_response(request_response)
        return response

