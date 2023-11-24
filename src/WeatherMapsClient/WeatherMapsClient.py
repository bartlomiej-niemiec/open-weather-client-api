from src.GenericClient.base_client import Client
from src.WeatherMapsClient.constants import Layers
from MapsCoordinates import MapParameters
from WeatherMap import BytesMapImage


class WeatherMapClient(Client):
    _map_area = 0
    _map_coordinates = 1
    _API_URL = "https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png"

    def get_map(self, layer: str, map_parameters: MapParameters):
        api_url = self._API_URL.format(
            layer=layer,
            x=map_parameters[self._map_coordinates].x,
            y=map_parameters[self._map_coordinates].y,
            z=map_parameters[self._map_area]
        )
        request_response = self._get_request(
            api_url,
            {}
        )

        return BytesMapImage(request_response.content)

    def get_maps_for_all_layers(self, map_parameters: MapParameters):
        maps = {attr: self.get_map(value, map_parameters) for attr, value in Layers().__dict__.items()}
        return maps
