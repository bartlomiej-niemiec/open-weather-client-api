from enum import IntEnum
from src.GenericClient.base_client import Client, parse_response
from _constants import DELETE_REQ_SUCCESS_CODE
from src.WeatherStationClient.StationParameters import StationParameters, RegisterStationParameters


class WeatherStationApiUrls(IntEnum):
    register_or_get_all = 0
    manage_station = 1


class WeatherStationManagementClient(Client):
    _API_URLS = [
        "http://api.openweathermap.org/data/3.0/stations",
        "http://api.openweathermap.org/data/3.0/stations/{station_id}"
    ]

    def register_station(self, station: RegisterStationParameters):
        response = self._post_request(
            url=self._API_URLS[WeatherStationApiUrls.register_or_get_all],
            data=station.__dict__
        )
        station_parameters = parse_response(response)
        return StationParameters(station_parameters)

    def delete_station(self, station_id):
        url_with_station_id = self._API_URLS[WeatherStationApiUrls.manage_station].format(
            station_id=station_id
        )
        response = self._delete_request(
            url=url_with_station_id,
            params={}
        )
        return response.status_code == DELETE_REQ_SUCCESS_CODE

    def get_all_stations(self):
        get_request_data = {}
        response = self._get_request(
            url=self._API_URLS[WeatherStationApiUrls.register_or_get_all],
            params=get_request_data
        )
        station_parameters_list = parse_response(response)
        station_object_list = [StationParameters(station_parameters) for station_parameters in
                               station_parameters_list]
        return station_object_list

    def get_station_info(self, station_id):
        url_with_station_id = self._API_URLS[WeatherStationApiUrls.manage_station].format(
            station_id=station_id
        )
        response = self._get_request(
            url=url_with_station_id,
            params={}
        )
        station_parameters = parse_response(response)
        return StationParameters(station_parameters)

    def update_station_info(self, station_id, station_params: RegisterStationParameters):
        url_with_station_id = self._API_URLS[WeatherStationApiUrls.manage_station].format(
            station_id=station_id
        )
        response = self._put_request(
            url=url_with_station_id,
            data=station_params.__dict__
        )
        station_parameters = parse_response(response)
        return StationParameters(station_parameters)