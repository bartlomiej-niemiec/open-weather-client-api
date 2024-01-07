from src.openweather_api.Common.GenericClient.BaseClient import Client
from src.openweather_api.WeatherMapsClient.Maps.LayersConstants import Layers
from src.openweather_api.WeatherMapsClient.Maps.MapCoordinates import MapCoordinates
from src.openweather_api.WeatherMapsClient.MapImage.BytesMapImage import BytesMapImage


class WeatherMapClient(Client):
    """Wrapper for OpenWeather Weather Maps 1.0 API."""
    _API_URL = "https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png"

    def get_map(self, layer: str, map_coordinates: MapCoordinates):
        """get map image object.

        :param layer: name of the layer.
        :param map_coordinates: data structure contains map coordinates.
        :return: map image object.
        """
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
        """get maps for all layers.

        :param map_coordinates: data structure contains map coordinates.
        :return: dict with map image objects.
        """
        maps = {attr: self.get_map(value, map_coordinates) for attr, value in Layers().__dict__.items()}
        return maps
