from src.GenericClient.Client import Client, parse_optional_parameters, merge_dicts, parse_response


class WeatherClient(Client):
    ALLOWED_OPTIONAL_PARS = ['unit', 'lang', 'format']
    API_URL = "https://api.openweathermap.org/data/2.5/weather"

    def current_weather_by_city_name(self, city_name, state_code=None, country_code=None, **kwargs):

        self._get_params_dict = {
            "q": (city_name, state_code, country_code)
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._get_request(
            self.API_URL
        )
        response = parse_response(request_response)
        return response

    def current_weather_by_city_id(self, city_id, **kwargs):

        self._get_params_dict = {
            "id": city_id
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._get_request(
            self.API_URL
        )
        response = parse_response(request_response)
        return response

    def current_weather_by_zip_code(self, zip_code, country_code, **kwargs):

        self._get_params_dict = {
            "zip": (zip_code, country_code)
        }
        self._add_optional_params_from_kwargs_to_request_params(kwargs)
        request_response = self._get_request(
            self.API_URL
        )
        response = parse_response(request_response)
        return response
