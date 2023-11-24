from enum import IntEnum
from src.GenericClient.base_client import Client, parse_response
from WeatherStation import RegisterStationParameters, Station
from _constants import DELETE_REQ_SUCCESS_CODE


class WeatherStationApiUrls(IntEnum):
    others = 0
    get_station = 1


class WeatherStationClient(Client):
    _API_URLS = [
        "http://api.openweathermap.org/data/3.0/stations",
        "http://api.openweathermap.org/data/3.0/stations/{station_id}"
    ]

    def register_station(self, station: RegisterStationParameters):
        post_request_data = {}
        post_request_data.update(station.__dict__)
        response = self._post_request(
            url=self._API_URLS[WeatherStationApiUrls.others],
            data=post_request_data
        )
        station_parameters = parse_response(response)
        return Station(station_parameters, self.api_key)

    def get_all_stations(self):
        get_request_data = {}
        response = self._get_request(
            url=self._API_URLS[WeatherStationApiUrls.others],
            params=get_request_data
        )
        station_parameters_list = parse_response(response)
        station_object_list = [Station(station_parameters, self.api_key) for station_parameters in
                               station_parameters_list]
        return station_object_list

    def get_station(self, station_id):
        url_with_station_id = self._API_URLS[WeatherStationApiUrls.get_station].format(
            station_id=station_id
        )
        response = self._get_request(
            url=url_with_station_id,
            params={}
        )
        station_parameters = parse_response(response)
        return Station(station_parameters, self.api_key)

    def delete_station(self, station_id):
        url_with_station_id = self._API_URLS[WeatherStationApiUrls.get_station].format(
            station_id=station_id
        )
        response = self._delete_request(
            url=url_with_station_id,
            params={}
        )
        return response.status_code == DELETE_REQ_SUCCESS_CODE
