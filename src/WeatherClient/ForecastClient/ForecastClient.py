from src.GenericClient._utils import parse_text_response
from src.GenericClient.base_client import Client
from src.WeatherClient._constants import Format, ALLOWED_OPTIONAL_PARS_FORECAST


class FiveDayForecastClient(Client):
    _API_URL = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self._allowed_optional_pras = ALLOWED_OPTIONAL_PARS_FORECAST

    def get_forecast_by_city_name(self, city_name: str, country_code: str = None, state_code=None, **kwargs):
        _get_params_dict = {
            "q": (city_name, state_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._get_request(
            self._API_URL,
            _get_params_dict
        )
        response = parse_text_response(
            request_response,
            parse_format=_get_params_dict.get("mode") or Format.DICT
        )
        return response

    def get_coordinates_by_zip_code(self, zip_code: str, country_code: str, **kwargs):
        _get_params_dict = {
            "zip": (zip_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._get_request(
            self._API_URL,
            _get_params_dict
        )
        response = parse_text_response(
            request_response,
            parse_format=_get_params_dict.get("mode") or Format.DICT
        )
        return response

    def get_name_of_location_by_city_id(self, city_id, **kwargs):
        _get_params_dict = {
            "id": city_id,
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._get_request(
            self._API_URL,
            _get_params_dict
        )
        response = parse_text_response(
            request_response,
            parse_format=_get_params_dict.get("mode") or Format.DICT
        )
        return response

