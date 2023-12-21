from src.GenericClient.base_client import Client
from src.WeatherMapsClient.constants import Layers
from src.WeatherMapsClient.MapArea import BaseMap
from WeatherMap import BytesMapImage


class WeatherMapClient(Client):
    _map_area = 0
    _map_coordinates = 1
    _API_URL = "https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png"

    def get_map(self, layer: str, map: BaseMap):
        api_url = self._API_URL.format(
            layer=layer,
            x=map.coordinates.x,
            y=map.coordinates.y,
            z=map.coordinates.z
        )
        request_response = self._get_request(
            api_url,
            {}
        )

        return BytesMapImage(request_response.content)

    def get_maps_for_all_layers(self, map: BaseMap):
        maps = {attr: self.get_map(value, map) for attr, value in Layers().__dict__.items()}
        return maps
