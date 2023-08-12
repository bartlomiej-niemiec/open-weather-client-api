import requests
from src.GenericClient.Client import Client
from _open_weather import Unit, Language

ALLOWED_OPTIONAL_PARS = ['unit', 'lang', 'format']
_CURRENT_WEATHER = "https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&lang={lang}&units={units}&mode={mode}"

class WeatherClient(Client):

    def current_weather(self, city, country, **kwargs):

        optional_args = self._parse_optional_parameters(
            ALLOWED_OPTIONAL_PARS,
            kwargs
        )

        http_request = _CURRENT_WEATHER.format(
            city=city,
            country=country,
            api_key=self.api_key,
            units=optional_args['unit'] or Unit.CELSIUS,
            lang=optional_args['lang'] or Language.English,
            mode=optional_args['format'] or '',
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for current weather"
        response = self._parse_response(response, )
        return response


if __name__ == "__main__":
    api_key = "API_KEY"
    response = WeatherClient(api_key).current_weather(
        "Sosnowiec",
        "PL",
        unit=Unit.CELSIUS,
        lang=Language.Polish
    )
