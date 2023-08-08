from src import GeocodingClient, WeatherClient


class ApiClient(WeatherClient, GeocodingClient):

    def __init__(self):
        super(self).__init__()
