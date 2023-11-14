from src.GenericClient.Client import Client, parse_response
from _open_weather import Format


class FiveDayForecastClient(Client):
    ALLOWED_OPTIONAL_PARS = ['units', 'lang', 'mode', 'limit', 'cnt']
    API_URL = "https://api.openweathermap.org/data/2.5/forecast"

    def get_forecast_by_city_name(self, city_name: str, country_code: str = None, state_code=None, **kwargs):
        self._get_params_dict = {
            "q": (city_name, state_code, country_code)
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._get_request(
            self.API_URL
        )
        response = parse_response(
            request_response,
            parse_format=self._get_params_dict.get("mode") or Format.DICT
        )
        return response

    def get_coordinates_by_zip_code(self, zip_code: str, country_code: str, **kwargs):
        self._get_params_dict = {
            "zip": (zip_code, country_code)
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._get_request(
            self.API_URL
        )
        response = parse_response(
            request_response,
            parse_format=self._get_params_dict.get("mode") or Format.DICT
        )
        return response

    def get_name_of_location_by_city_id(self, city_id, **kwargs):
        self._get_params_dict = {
            "id": city_id,
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._get_request(
            self.API_URL
        )
        response = parse_response(
            request_response,
            parse_format=self._get_params_dict.get("mode") or Format.DICT
        )
        return response

