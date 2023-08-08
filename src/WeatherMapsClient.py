from datetime import datetime
import requests
from src.GenericClient.Client import Client
from _open_weather import OpenWeatherRequest
from io import BytesIO
from PIL import Image
import os

ALLOWED_OPTIONAL_PARS = ['unit', 'lang', 'format', 'limit']


class Layers:
    _clouds = "clouds_new"
    _precipitation = "precipitation_new"
    _sea_level_pressure = "pressure_new"
    _wind_speed = "wind_new"
    _temperature = "temp_new"

    _list_layers = [
        _clouds,
        _precipitation,
        _sea_level_pressure,
        _wind_speed,
        _temperature,
    ]

    def __init__(self):
        self._iter_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter_index < len(self._list_layers):
            layer = self._list_layers[self._iter_index]
            self._iter_index += 1
            return layer
        else:
            raise StopIteration

    @property
    def clouds(self):
        return self._clouds

    @property
    def precipitation(self):
        return self._precipitation

    @property
    def sea_level_pressure(self):
        return self._sea_level_pressure

    @property
    def wind_speed(self):
        return self._wind_speed

    @property
    def temperature(self):
        return self._temperature


class ZoomLevelZet:
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9


class WeatherMapClient(Client):

    def _parse_png_map(self, data):
        return Image.open(BytesIO(data))

    def get_map(self, layer, z, x, y, **kwargs):

        http_request = OpenWeatherRequest.WEATHER_MAP.format(
            layer=layer,
            x=x,
            y=y,
            z=z,
            api_key=self.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for current weather"
        img = self._parse_png_map(response.content)
        img.save(os.getcwd() + '\map_{layer}_{date}.png'.format(
            layer=layer,
            date=datetime.today().strftime('%Y-%m-%d')
        ), 'png')

    def get_all_maps(self, z, x, y, **kwargs):
        for layer in Layers():
            self.get_map(layer, z, x, y, **kwargs)


if __name__ == "__main__":
    api_key = "API_KEY"
    WeatherMapClient(api_key).get_all_maps(
        ZoomLevelZet.two,
        2,
        2
    )
