import requests
from src.GenericClient.base_client import Client
from WeatherStation import RegisterStationParameters, Station


class WeatherStationClient:
    _HEADERS = {'Content-Type': 'application/json'}
    _WEATHER_STATION_URL = "http://api.openweathermap.org/data/3.0/stations"
    _GET_ALL_STATIONS = "http://api.openweathermap.org/data/3.0/stations?appid={api_key}"
    _GET_STATION_INFO = "http://api.openweathermap.org/data/3.0/stations/{station_id}?appid={api_key}"

    def __init__(self, api_client: Client):
        self._api_client = api_client

    def register_station(self, station: RegisterStationParameters):
        try:
            response = requests.post(self._WEATHER_STATION_URL, data=station.__dict__, headers=self._HEADERS)
        except:
            raise "Error while requesting for coordinates"
        response = self._api_client._parse_response(response)

        return Station(response, self._api_client)

    def get_all_stations(self):
        http_request = self._GET_ALL_STATIONS.format(
            api_key=self._api_client.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for list of all stations"
        response = self._api_client._parse_response(response)
        registered_stations = []
        for station in response:
            registered_stations.append(Station(station, self._api_client))
        return registered_stations

    def get_station(self, station_id):
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
