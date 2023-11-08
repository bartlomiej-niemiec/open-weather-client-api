from typing import List
from src._open_weather import Format
import json


class Client:

    def __init__(self, api_key):
        self.api_key = api_key


    def _parse_response(self, response, parse_format=None):
        if response.text:
            if not parse_format:
                json_response = json.loads(response.text)
                return json_response
            elif parse_format == Format.JSON:
                return response.json()
            elif parse_format == Format.XML:
                return response.text

    def _parse_optional_parameters(self, allowed_optional_pars, pars):
        optional_args = {par: "" for par in allowed_optional_pars}

        for key, item in pars.items():
            if key not in allowed_optional_pars:
                raise f"Following argument '{key}' is not supported"
            else:
                optional_args[key] = item

        return optional_args
