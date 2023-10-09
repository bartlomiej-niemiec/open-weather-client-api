from Measurment import StationMeasurement
import requests
from src.GenericClient.Client import Client
from WeatherStation import Station, create_station_from_json

_REGISTER_STATION = "https://api.openweathermap.org/data/3.0/stations?appid={api_key}"
_SEND_MEASUREMENT = "https://api.openweathermap.org/data/3.0/measurements?appid={api_key}"
_GET_MEASUREMENT = "http://api.openweathermap.org/data/3.0/measurements?appid={api_key}&station_id={station_id}&type={type}&limit={limit}&from={from}&to={to}"
_GET_ALL_STATIONS = "https://api.openweathermap.org/data/3.0/stations?appid={api_key}"
_GET_STATION_INFO = "http://api.openweathermap.org/data/3.0/stations/{station_id}?appid={api_key}"
_UPDATE_STATION_INFO = "http://api.openweathermap.org/data/3.0/stations/{station_id}?appid={api_key}"
_DELETE_STATION = "http://api.openweathermap.org/data/3.0/stations/{station_id}?appid={api_key}"

class WeatherStationClient(Client):

    def register_station(self, station: Station):
        http_request = _REGISTER_STATION.format(
            api_key=self.api_key
        )
        try:
            response = requests.post(http_request, json=station)
        except:
            raise "Error while requesting for coordinates"
        return response

    def send_measurement(self, StationMeasurement):
        #TO DO
        pass

    def get_measurement(self):
        #TO DO
        pass

    def get_all_stations(self):
        http_request = _GET_ALL_STATIONS.format(
            api_key=self.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for list of all stations"
        response = self._parse_response(response)
        return response

    def get_station_info(self, station_id):
        http_request = _GET_STATION_INFO.format(
            station_id=station_id,
            api_key=self.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for information about station "
        response = self._parse_response(response)
        station = None
        if response:
            station = create_station_from_json(response)
        return station or response

    def update_station_info(self, station, station_id):
        http_request = _UPDATE_STATION_INFO.format(
            station_id=station_id,
            api_key=self.api_key
        )
        try:
            response = requests.put(http_request, json=station)
        except:
            raise "Error while requesting for update information about station "
        response = self._parse_response(response)
        return response

    def delete_station_info(self, station_id):
        http_request = _DELETE_STATION.format(
            station_id=station_id,
            api_key=self.api_key
        )
        try:
            response = requests.delete(http_request)
        except:
            raise "Error while requesting for update information about station "
        response = self._parse_response(response)
        return response


if __name__ == "__main__":
    api_key = "API_KEY"
    client = WeatherStationClient(api_key)
    station = Station(
        external_id='123',
        name="Test Station",
        latitude=0.0,
        longitude=0.0,
        altitude=150
    )