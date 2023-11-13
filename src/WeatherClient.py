from src.GenericClient.Client import Client, parse_optional_parameters, merge_dicts, parse_response
from _open_weather import Unit, Language


class WeatherClient(Client):
    ALLOWED_OPTIONAL_PARS = ['unit', 'lang', 'format']
    _DEFAULT_URL = "https://api.openweathermap.org/data/2.5/weather"

    def current_weather_by_city_name(self, city_name, state_code=None, country_code=None, **kwargs):

        required_parameters = {
            "q": (city_name, state_code, country_code)
        }

        optional_args = parse_optional_parameters(
            self.ALLOWED_OPTIONAL_PARS,
            kwargs
        )

        self._get_params_dict = merge_dicts(
            required_parameters,
            optional_args
        )

        try:
            request_response = self._get_request()
        except:
            raise "Error while requesting for current weather"
        response = parse_response(request_response)
        return response

    def current_weather_by_city_id(self, city_id, **kwargs):

        required_parameters = {
            "id": city_id
        }

        optional_args = parse_optional_parameters(
            self.ALLOWED_OPTIONAL_PARS,
            kwargs
        )

        self._get_params_dict = merge_dicts(
            required_parameters,
            optional_args
        )

        try:
            request_response = self._get_request()
        except:
            raise "Error while requesting for current weather"
        response = parse_response(request_response)
        return response

    def current_weather_by_zip_code(self, zip_code, country_code, **kwargs):

        required_parameters = {
            "zip": (zip_code, country_code)
        }

        optional_args = parse_optional_parameters(
            self.ALLOWED_OPTIONAL_PARS,
            kwargs
        )

        self._get_params_dict = merge_dicts(
            required_parameters,
            optional_args
        )

        try:
            request_response = self._get_request()
        except:
            raise "Error while requesting for current weather"
        response = parse_response(request_response)
        return response

    def _get_api_url(self):
        return self._DEFAULT_URL



if __name__ == "__main__":
    api_key = "7d31a3f3f66a92ac5744ea0572e5bcf5"
    client = WeatherClient(api_key)
    response = client.current_weather_by_city_name(
        "Sosnowiec",
        unit=Unit.CELSIUS,
        lang=Language.Polish
    )
    print(response)
    response = client.current_weather_by_city_name(
        "Sosnowiec",
        country_code="PL",
        unit=Unit.CELSIUS,
        lang=Language.Polish
    )
    print(response)
    response = client.current_weather_by_city_name(
        "Sosnowiec",
        country_code="PL",
        state_code="PL-24",
        unit=Unit.CELSIUS,
        lang=Language.Polish
    )
    print(response)
    warsaw_id = 756135
    response = client.current_weather_by_city_id(city_id=warsaw_id)
    print(response)
    response = client.current_weather_by_zip_code(zip_code=94040, country_code="us")
    print(response)