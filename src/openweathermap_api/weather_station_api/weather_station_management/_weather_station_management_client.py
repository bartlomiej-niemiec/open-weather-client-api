from src.openweathermap_api.common import Client, parse_request_response_to_format
from src.openweathermap_api.weather_station_api.weather_station_management._station_parameters import \
    StationParameters, RegisterStationParameters
from src.openweathermap_api.weather_station_api.weather_station_management._weather_station_management_utils import \
    WeatherStationManagementApiUrls

_DELETE_REQ_SUCCESS_CODE = 204


class WeatherStationManagementClient(Client):
    """Wrapper for OpenWeather Weather Stations API. - Station Management."""
    _API_URLS = [
        "http://api.openweathermap.org/data/3.0/stations",
        "http://api.openweathermap.org/data/3.0/stations/{station_id}"
    ]

    def register_station(self, station: RegisterStationParameters):
        """register station.

        :param station: data structure with station parameters.
        :return: parameters of registered station.
        """
        response = self._send_request(
            'POST',
            url=self._API_URLS[WeatherStationManagementApiUrls.register_or_get_all],
            data=station.__dict__
        )
        station_parameters = parse_request_response_to_format(response)
        return StationParameters(station_parameters)

    def delete_station(self, station_id):
        """delete station.

        :param station_id: id of the station to be deleted.
        :return: true if delete succeed
        """
        url_with_station_id = self._API_URLS[WeatherStationManagementApiUrls.manage_station].format(
            station_id=station_id
        )
        response = self._send_request(
            'DELETE',
            url=url_with_station_id,
            data={}
        )
        return response.status_code == _DELETE_REQ_SUCCESS_CODE

    def get_all_stations(self):
        """get all registered stations.

        :return: list of all registered stations.
        """
        get_request_data = {}
        response = self._send_request(
            'GET',
            url=self._API_URLS[WeatherStationManagementApiUrls.register_or_get_all],
            data=get_request_data
        )
        station_parameters_list = parse_request_response_to_format(response)
        station_object_list = [StationParameters(station_parameters) for station_parameters in
                               station_parameters_list]
        return station_object_list

    def get_station_info(self, station_id):
        """get information about single station.

        :param station_id: id of registered station.
        :return: parameters of registered station.
        """
        url_with_station_id = self._API_URLS[WeatherStationManagementApiUrls.manage_station].format(
            station_id=station_id
        )
        response = self._send_request(
            'GET',
            url=url_with_station_id,
            data={}
        )
        station_parameters = parse_request_response_to_format(response)
        return StationParameters(station_parameters)

    def update_station_info(self, station_id, station_params: RegisterStationParameters):
        """update parameters of already registered station.

        :param station_id: id of registered station.
        :param station_params: new station parameters.
        :return: updated station parameters.
        """
        url_with_station_id = self._API_URLS[WeatherStationManagementApiUrls.manage_station].format(
            station_id=station_id
        )
        response = self._send_request(
            'PUT',
            url=url_with_station_id,
            data=station_params.__dict__
        )
        station_parameters = parse_request_response_to_format(response)
        return StationParameters(station_parameters)
