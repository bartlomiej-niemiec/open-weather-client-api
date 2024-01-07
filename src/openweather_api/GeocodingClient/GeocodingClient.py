from typing import Any
from src.openweather_api.Utils.RequestResponseParsing import parse_text_response_to_format
from src.openweather_api.Common.GenericClient.BaseClient import Client
from src.openweather_api.GeocodingClient.GeocodingUtils import ALLOWED_OPTIONAL_PARS, GeocodingUrls


class GeocodingApiClient(Client):
    """Wrapper for OpenWeather Geocoding API."""

    _API_URLS = [
        "https://api.openweathermap.org/geo/1.0/direct",
        "http://api.openweathermap.org/geo/1.0/zip",
        "http://api.openweathermap.org/geo/1.0/reverse"
    ]

    def __init__(self, api_key: str):
        """Initialization of Geocoding API client.

        :param api_key: OpenWeather API Key.
        """
        super().__init__(api_key)
        self._allowed_optional_pras = ALLOWED_OPTIONAL_PARS

    def get_coordinates_by_location_name(self, city_name: str, country_code: str = None, state_code=None, **kwargs) -> \
    dict[str, Any]:
        """Get coordinates by location.

        :param city_name: name of the city.
        :param country_code: country code etc. 'UK'. Defaults to None.
        :param state_code: state code - only for US. Defaults to None.
        :param kwargs: optional parameters listed below
            limit: number of the locations - up to 5.
        :return: api response.
        """
        _get_params_dict = {
            "q": (city_name, state_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URLS[GeocodingUrls.by_location_name],
            _get_params_dict
        )
        response = parse_text_response_to_format(request_response)
        return response

    def get_coordinates_by_zip_code(self, zip_code: str, country_code: str, **kwargs) -> dict[str, Any]:
        """Get coordinates by zip code.

        :param zip_code: zip/post code referred to ISO 3166.
        :param country_code: country code etc. 'UK'.
        :param kwargs: optional parameters listed below
            limit: number of the locations - up to 5.
        :return: api response.
        """
        _get_params_dict = {
            "zip": (zip_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URLS[GeocodingUrls.by_zip_code],
            _get_params_dict
        )
        response = parse_text_response_to_format(request_response)
        return response

    def get_name_of_location_by_coordiantes(self, latitude, longitude, **kwargs) -> list:
        """Get location name by passing it geographical coordinates.

        :param latitude: geographical coordinates - latitude
        :param longitude: geographical coordinates - longitude
        :param kwargs: optional parameters listed below
            limit: number of the locations - up to 5.
        :return: api response.
        """
        _get_params_dict = {
            "lat": latitude,
            "lon": longitude
        }
        self._verify_and_add_optional_params_to_request(kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URLS[GeocodingUrls.reverse],
            _get_params_dict
        )
        response = parse_text_response_to_format(request_response)
        return response
