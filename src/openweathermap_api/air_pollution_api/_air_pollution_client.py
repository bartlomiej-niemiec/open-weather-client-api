from src.openweathermap_api.air_pollution_api._air_pollution_utils import AirPollutionUrls, parse_air_polution_response
from src.openweathermap_api.geocoding_api import GeocodingClient
from src.openweathermap_api.common import Client
from src.openweathermap_api.utils import UTCtoUnixTime


class AirPollutionClient(Client):
    """Wrapper for OpenWeather AirPollution API."""

    _API_URLS = [
        "https://api.openweathermap.org/data/2.5/air_pollution",
        "https://api.openweathermap.org/data/2.5/air_pollution/forecast",
        "http://api.openweathermap.org/data/2.5/air_pollution/history"
    ]

    def __init__(self, api_key):
        """Initialization of AirPollution API client.

        Args:
            api_key str: OpenWeather API Key.
        """
        super().__init__(api_key)
        self._cache = {}
        self._geocoding_client = GeocodingClient(api_key)

    def current_air_pollution_by_location(self, city_name: str, country_code=None, state_code=None, **kwargs):
        """Get current air pollution.

        Args:
            city_name (str): name of the city
            country_code (str, optional): country code etc. 'UK'. Defaults to None.
            state_code (str, optional): state code - only for US. Defaults to None.

        Returns:
            dict: air pollution data.
        """
        lat, lon = self._get_coordinates(city_name, country_code, state_code)

        _get_params_dict = {
            "lat": lat,
            "lon": lon
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URLS[AirPollutionUrls.current],
            _get_params_dict
        )
        response = parse_air_polution_response(request_response)
        return response

    def forecast_air_pollution(self, city_name: str, country_code=None, state_code=None, **kwargs):
        """Get forecast air pollution.

        Args:
            city_name (str): name of the city
            country_code (str, optional): country code etc. 'UK'. Defaults to None.
            state_code (str, optional): state code - only for US. Defaults to None.

        Returns:
            dict: forecast data.
        """
        lat, lon = self._get_coordinates(city_name, country_code, state_code)
        _get_params_dict = {
            "lat": lat,
            "lon": lon
        }
        self._verify_and_add_optional_params_to_request(kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URLS[AirPollutionUrls.forecast],
            _get_params_dict
        )
        response = parse_air_polution_response(request_response)
        return response

    def historical_air_pollution(self, city_name: str, *, start: UTCtoUnixTime, end: UTCtoUnixTime, country_code=None, state_code=None, **kwargs):
        """Get historical info about air pollution.

        Args:
            city_name (str): name of the city
            start (UTCtoUnixTime): start timestamp range
            end (UTCtoUnixTime): end timestamp range
            country_code (str, optional): country code etc. 'UK'. Defaults to None.
            state_code (str, optional): state code - only for US. Defaults to None.

        Returns:
            dict: historical data.
        """
        lat, lon = self._get_coordinates(city_name, country_code, state_code)
        _get_params_dict = {
            "lat": lat,
            "lon": lon,
            "start": str(start),
            "end": str(end)
        }
        self._verify_and_add_optional_params_to_request(_get_params_dict, kwargs)
        request_response = self._send_request(
            'GET',
            self._API_URLS[AirPollutionUrls.forecast],
            _get_params_dict
        )
        response = parse_air_polution_response(request_response)
        return response

    def _get_coordinates(self, city_name: str, country_code=None, state_code=None):
        """Get latitude and longitude of desired localization.

        Args:
            city_name (str): name of the city
            country_code (str, optional): country code etc. 'UK'. Defaults to None.
            state_code (str, optional): state code - only for US. Defaults to None.

        Returns:
            tuple: latitude and longitude
        """
        SINGLE_LOCATION = 0
        if not (coordinates := self._cache.get((city_name, country_code, state_code))):
            coordinates = (self._geocoding_client.get_coordinates_by_location_name(city_name, country_code, state_code))[SINGLE_LOCATION]
            self._cache[(city_name, country_code, state_code)] = coordinates

        return coordinates["lat"], coordinates["lon"]






