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

    _IMG_FILE_TEMPLATE = '\map_{layer}_{date}.png'

    def _parse_png_map(self, data):
        return Image.open(BytesIO(data))

    def save_to_png(self, data: bytes, path: str, name: str):
        img = self._parse_png_map(data)
        path = path if path[-1] != "\\" else path[:-1]
        img.save(path + name, 'png')

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

        return response

    def get_all_maps(self, z, x, y, **kwargs):
        resp_dict = {layer: self.get_map(layer, z, x, y, **kwargs) for layer in Layers()}
        return resp_dict


if __name__ == "__main__":
    api_key = "7d31a3f3f66a92ac5744ea0572e5bcf5"
    response = WeatherMapClient(api_key).get_map(
        Layers._sea_level_pressure,
        ZoomLevelZet.two,
        2,
        2
    )
