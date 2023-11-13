import requests
from src.GenericClient.Client import Client
from _open_weather import Unit, Language, Format


class ForecastClient(Client):

    ALLOWED_OPTIONAL_PARS = ['unit', 'lang', 'format', 'limit']
    _FORECAST = "https://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={api_key}&mode={mode}&cnt={cnt}&units={units}&lang={lang}"

    def get_forecast(self, city, country, **kwargs):

        optional_args = _parse_optional_parameters(
            self.ALLOWED_OPTIONAL_PARS,
            kwargs
        )
        http_request = self._FORECAST.format(
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
        response = _parse_response(response, optional_args['format'])
        return response


if __name__ == "__main__":
    api_key = "API_KEY"
    response = ForecastClient(api_key).get_forecast(
        "Sosnowiec",
        "PL",
        format=Format.XML
    )
