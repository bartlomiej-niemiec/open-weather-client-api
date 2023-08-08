import requests
from src.GenericClient.Client import Client
from _open_weather import OpenWeatherRequest, Unit, Language, Format

ALLOWED_OPTIONAL_PARS = ['unit', 'lang', 'format', 'limit']


class ForecastClient(Client):

    def get_forecast(self, city, country, **kwargs):

        optional_args = self._parse_optional_parameters(
            ALLOWED_OPTIONAL_PARS,
            kwargs
        )
        http_request = OpenWeatherRequest.FORECAST.format(
            city=city,
            country=country,
            api_key=self.api_key,
            units=optional_args['unit'] or Unit.CELSIUS,
            lang=optional_args['lang'] or Language.English,
            mode=optional_args['format'],
            cnt=optional_args['limit'] or '',
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for current weather"
        response = self._parse_response(response, optional_args['format'])
        return response


if __name__ == "__main__":
    api_key = "API_KEY"
    response = ForecastClient(api_key).get_forecast(
        "Sosnowiec",
        "PL",
        format=Format.XML
    )
    print(response)
