import requests
from src.GenericClient.Client import Client
from io import BytesIO
from PIL import Image
from Layers import Layers
from ZoomLevel import ZetZoomLevel

ALLOWED_OPTIONAL_PARS = ['unit', 'lang', 'format', 'limit']
_WEATHER_MAP = "https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={api_key}"

class WeatherMapClient(Client):
    _IMG_FILE_TEMPLATE = '\map_{layer}_{date}.png'

    def _parse_png_map(self, data):
        return Image.open(BytesIO(data))

    def save_to_png(self, data: bytes, path: str, name: str):
        img = self._parse_png_map(data)
        path = path if path[-1] != "\\" else path[:-1]
        img.save(path + name, 'png')

    def get_map(self, layer, z, x, y, **kwargs):

        http_request = _WEATHER_MAP.format(
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
    api_key = "API_KEY"
    response = WeatherMapClient(api_key).get_map(
        Layers._sea_level_pressure,
        ZetZoomLevel.two,
        2,
        2
    )
