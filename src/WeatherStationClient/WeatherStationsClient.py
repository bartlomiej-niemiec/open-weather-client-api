import requests
from src._utils import UnixTime
from src.GenericClient.Client import Client
from WeatherStation import Station

_REGISTER_STATION = "https://api.openweathermap.org/data/3.0/stations"
_SEND_MEASUREMENT = "https://api.openweathermap.org/data/3.0/measurements"
_GET_MEASUREMENT = "http://api.openweathermap.org/data/3.0/measurements?station_id={station_id}&type={type}&limit={limit}&from={from}&to={to}"
_GET_ALL_STATIONS = "https://api.openweathermap.org/data/3.0/stations"
_GET_STATION_INFO = "http://api.openweathermap.org/data/3.0/stations/{station_info}"
_UPDATE_STATION_INFO = "http://api.openweathermap.org/data/3.0/stations/{station_info}"
_DELETE_STATION = "http://api.openweathermap.org/data/3.0/stations/{station_info}"

class WeatherStationClient(Client):

    def register_station(self, station: Station):
        #TO DO

    def send_measurement(self):
        #TO DO

    def get_send_measurement(self):
        #TO DO

    def get_all_stations(self):
        #TO DO

    def get_station_info(self):
        #TO DO

    def update_station_info(self):
        #TO DO

    def delete_station_info(self):
        #TO DO


if __name__ == "__main__":
    api_key = "API_KEY"
    response = WeatherStationClient(api_key)