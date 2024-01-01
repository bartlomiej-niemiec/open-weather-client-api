from src.GenericClient._utils import parse_text_response
from src.GenericClient.base_client import Client
from _constants import ALLOWED_OPTIONAL_PARS_WEATHER

class WeatherClient(Client):
    _API_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self._allowed_optional_pras = ALLOWED_OPTIONAL_PARS_WEATHER

    def current_weather_by_city_name(self, city_name, state_code=None, country_code=None, **kwargs):

        _get_params_dict = {
            "q": (city_name, state_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URL,
            _get_params_dict
        )
        response = parse_text_response(request_response)
        return response

    def current_weather_by_city_id(self, city_id, **kwargs):

        _get_params_dict = {
            "id": city_id
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URL,
            _get_params_dict
        )
        response = parse_text_response(request_response)
        return response

    def current_weather_by_zip_code(self, zip_code, country_code, **kwargs):

        _get_params_dict = {
            "zip": (zip_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URL,
            _get_params_dict
        )
        response = parse_text_response(request_response)
        return response

