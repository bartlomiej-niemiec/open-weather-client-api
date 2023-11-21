from src.GenericClient.base_client import Client
from Layers import Layers
from MapsCoordinates import MapCoordinates, MapParameters
from WeatherMap import MapImage


class WeatherMapClient(Client):
    _map_area = 0
    _map_coordinates = 1
    API_URL = "https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png"

    def get_map(self, layer: str, map_parameters: MapParameters):
        api_url = self.API_URL.format(
            layer=layer,
            x=map_parameters[self._map_coordinates].x,
            y=map_parameters[self._map_coordinates].y,
            z=map_parameters[self._map_area]
        )
        request_response = self._get_request(
            api_url,
            {}
        )

        return MapImage(request_response.content)

    def get_maps_for_all_layers(self, map_coordinates: MapCoordinates):
        maps = {attr: self.get_map(value, map_coordinates) for attr, value in Layers().__dict__.items()}
        return maps