import requests
from GenericClient.Client import Client
from _open_weather import OpenWeatherRequest


class GeocodingApiClient(Client):

    def get_coordinates(self, city: str, country: str, limit: int) -> tuple[float, float]:
        http_request = OpenWeatherRequest.GET_COORDINATE.format(
            city=city,
            country=country,
            limit=limit,
            api_key=self.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for coordinates"
        response = self._parse_response(response)
        return response["lat"], response["lon"]


if __name__ == "__main__":
    api_key = "API_KEY"
    response = GeocodingApiClient(api_key).get_coordinates("Sosnowiec", "PL", 1)
    print(response)
