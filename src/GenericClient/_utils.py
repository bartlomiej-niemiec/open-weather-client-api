from src.GenericClient.exceptions import UnknownOptionalParameter
from src.WeatherClient._constants import Format
import json

def parse_optional_parameters(allowed_optional_pars, pars):
    optional_args = {}
    for key, item in pars.items():
        if key not in allowed_optional_pars:
            raise UnknownOptionalParameter(f"Unknown parameter: '{key}'")
        else:
            optional_args[key] = item

    return optional_args


def parse_text_response(response, parse_format=Format.DICT):
    text_response = response.text
    if text_response:
        parsed_response = None
        if parse_format == Format.DICT:
            parsed_response = json.loads(text_response)
        elif parse_format == Format.JSON:
            parsed_response = response.json()
        elif parse_format == Format.XML:
            parsed_response = text_response
        return parsed_response