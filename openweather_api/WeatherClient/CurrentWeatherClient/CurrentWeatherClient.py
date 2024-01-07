from openweather_api.Utils.RequestResponseParsing import parse_text_response_to_format
from openweather_api.Common.GenericClient.BaseClient import Client
from openweather_api.WeatherClient.Constants import ALLOWED_OPTIONAL_PARS_WEATHER


class CurrentWeatherClient(Client):
    """Wrapper for OpenWeather Current Weather API."""
    _API_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str):
        """Initialization of Current Weather API client.

        :param api_key: OpenWeather API Key.
        """
        super().__init__(api_key)
        self._allowed_optional_pars = ALLOWED_OPTIONAL_PARS_WEATHER

    def current_weather_by_location(self, city_name, state_code=None, country_code=None, **kwargs):
        """get current weather by location.

        :param city_name: name of the city
        :param state_code: country code etc. 'UK'. Defaults to None.
        :param country_code: state code - only for US. Defaults to None.
        :param kwargs: optional parameters listed below
            units: unit of measurement - Kelvin, Fahrenheit.
            lang: language of output.
            mode: response format.
        :return: api response.
        """
        _get_params_dict = {
            "q": (city_name, state_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URL,
            _get_params_dict
        )
        response = parse_text_response_to_format(request_response)
        return response

    def current_weather_by_city_id(self, city_id, **kwargs):
        """get current weather by city id.

        :param city_id: city id - download list of city id on openweathermap.org
        :param kwargs: optional parameters listed below
            units: unit of measurement - Kelvin, Fahrenheit.
            lang: language of output.
            mode: response format.
        :return: api response.
        """
        _get_params_dict = {
            "id": city_id
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URL,
            _get_params_dict
        )
        response = parse_text_response_to_format(request_response)
        return response

    def current_weather_by_zip_code(self, zip_code, country_code, **kwargs):
        """get current weather by zip code.

        :param zip_code: zip/post code referred to ISO 3166.
        :param country_code: country code etc. 'UK'.
        :param kwargs: optional parameters listed below
            units: unit of measurement - Kelvin, Fahrenheit.
            lang: language of output.
            mode: response format.
        :return: api response.
        """
        _get_params_dict = {
            "zip": (zip_code, country_code)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URL,
            _get_params_dict
        )
        response = parse_text_response_to_format(request_response)
        return response
