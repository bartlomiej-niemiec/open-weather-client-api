from src.utils.GenericClient.BaseClient import Client
from src.WeatherMapsClient.Maps.LayersConstants import Layers
from src.WeatherMapsClient.Maps.MapCoordinates import MapCoordinates
from src.WeatherMapsClient.MapImage.WeatherMap import BytesMapImage


class WeatherMapClient(Client):
    _API_URL = "https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png"

    def get_map(self, layer: str, map_coordinates: MapCoordinates):
        api_url = self._API_URL.format(
            layer=layer,
            x=map_coordinates.x,
            y=map_coordinates.y,
            z=map_coordinates.z
        )
        request_response = self._send_request(
            'GET',
            api_url,
            {}
        )

        return BytesMapImage(request_response.content)

    def get_maps_for_all_layers(self, map_coordinates: MapCoordinates):
        maps = {attr: self.get_map(value, map_coordinates) for attr, value in Layers().__dict__.items()}
        return maps
