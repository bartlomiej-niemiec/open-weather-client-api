from typing import Any
import requests
from src.GenericClient.Client import Client

ALLOWED_OPTIONAL_PARS = ['limit']
_GET_COORDINATE = "https://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit={limit}&appid={api_key}"

class GeocodingApiClient(Client):

    def get_coordinates(self, city: str, country: str, **kwargs) -> dict[str, Any]:
        optional_args = self._parse_optional_parameters(
            ALLOWED_OPTIONAL_PARS,
            kwargs
        )
        http_request = _GET_COORDINATE.format(
            city=city,
            country=country,
            limit=optional_args['limit'],
            api_key=self.api_key
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for coordinates"
        response = self._parse_response(response)
        return {
            'lat': response["lat"],
            'lon': response["lon"]
        }


if __name__ == "__main__":
    api_key = "API_KEY"
    response = GeocodingApiClient(api_key).get_coordinates("Sosnowiec", "PL")
