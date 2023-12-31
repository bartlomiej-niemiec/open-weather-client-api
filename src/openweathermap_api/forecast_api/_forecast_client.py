from src.openweathermap_api.common import Client, parse_request_response_to_format

_ALLOWED_OPTIONAL_PARS_FORECAST = ['units', 'lang', 'mode', 'cnt']

class FiveDayForecastClient(Client):

    """Wrapper for OpenWeather 5-day weather forecast api."""

    _API_URL = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, api_key: str):
        """Initialization of Current Weather API client.

        :param api_key: OpenWeather API Key.
        """
        super().__init__(api_key)
        self._allowed_optional_pras = _ALLOWED_OPTIONAL_PARS_FORECAST

    def get_forecast_by_city_name(self, city_name: str, country_code: str = None, state_code=None, **kwargs):
        """get forecast by city name.

        :param city_name: name of the city
        :param country_code: country code etc. 'UK'. Defaults to None.
        :param state_code: state code - only for US. Defaults to None.
        :param kwargs: optional parameters listed below
            units: unit of measurement - Kelvin, Fahrenheit.
            lang: language of output.
            mode: response format.
            cnt: number of timestamps
        :return: api response.
        """
        _get_params_dict = {
            "q": (city_name, state_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            "GET",
            self._API_URL,
            _get_params_dict
        )
        response = parse_request_response_to_format(
            request_response,
            parse_format=_get_params_dict.get("mode") or Format.DICT
        )
        return response

    def get_forecast_by_zip_code(self, zip_code: str, country_code: str, **kwargs):
        """get forecast by zip code.

        :param zip_code: zip/post code referred to ISO 3166.
        :param country_code: country code etc. 'UK'.
        :param kwargs: optional parameters listed below
            units: unit of measurement - Kelvin, Fahrenheit.
            lang: language of output.
            mode: response format.
            cnt: number of timestamps
        :return: api response.
        """
        _get_params_dict = {
            "zip": (zip_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            "GET",
            self._API_URL,
            _get_params_dict
        )
        response = parse_request_response_to_format(
            request_response,
            parse_format=_get_params_dict.get("mode") or Format.DICT
        )
        return response

    def get_forecast_by_city_id(self, city_id, **kwargs):
        """get forecast by city id.

        :param city_id: city id - download list of city id on openweathermap.org
        :param kwargs: optional parameters listed below
            units: unit of measurement - Kelvin, Fahrenheit.
            lang: language of output.
            mode: response format.
            cnt: number of timestamps
        :return: api response.
        """
        _get_params_dict = {
            "id": city_id,
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            "GET",
            self._API_URL,
            _get_params_dict
        )
        response = parse_request_response_to_format(
            request_response,
            parse_format=_get_params_dict.get("mode") or Format.DICT
        )
        return response

