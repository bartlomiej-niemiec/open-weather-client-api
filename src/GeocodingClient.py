from typing import Any

import requests
from GenericClient.Client import Client
from _open_weather import OpenWeatherRequest

ALLOWED_OPTIONAL_PARS = ['limit']


class GeocodingApiClient(Client):

    def get_coordinates(self, city: str, country: str, **kwargs) -> dict[str, Any]:
        optional_args = self._parse_optional_parameters(
            ALLOWED_OPTIONAL_PARS,
            kwargs
        )
        http_request = OpenWeatherRequest.GET_COORDINATE.format(
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
    api_key = "7d31a3f3f66a92ac5744ea0572e5bcf5"
    response = GeocodingApiClient(api_key).get_coordinates("Sosnowiec", "PL")
    print(response)
