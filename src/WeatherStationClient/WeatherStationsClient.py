import requests
from src.GenericClient.Client import Client
from WeatherStation import RegisteredStation


class WeatherStationClient:
    _REGISTER_STATION = "http://api.openweathermap.org/data/3.0/stations?appid={api_key}"
    _GET_ALL_STATIONS = "http://api.openweathermap.org/data/3.0/stations?appid={api_key}"
    _GET_STATION_INFO = "http://api.openweathermap.org/data/3.0/stations/{station_id}?appid={api_key}"

    def __init__(self, api_client: Client):
        self._api_client = api_client

    def register_station(self, station: RegisteredStation):
        http_request = self._REGISTER_STATION.format(
            api_key=self._api_client.api_key
        )
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(http_request, data=station.toJSON(), headers=headers)
        except:
            raise "Error while requesting for coordinates"
        response = self._api_client._parse_response(response)
        return response

    def get_all_stations(self):
        http_request = self._GET_ALL_STATIONS.format(
            api_key=self._api_client.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for list of all stations"
        response = self._api_client._parse_response(response)
        return response

    def get_station_info(self, station_id):
        http_request = self._GET_STATION_INFO.format(
            station_id=station_id,
            api_key=self._api_client.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for information about station "
        response = self._api_client._parse_response(response)
        return response
