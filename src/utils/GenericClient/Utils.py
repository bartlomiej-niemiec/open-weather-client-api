from src.utils.GenericClient.Exceptions import UnknownOptionalParameter
from src.WeatherClient.Constants import Format
import json


def verify_optional_parameters(allowed_optional_pars, pars):
    """Check if passed optional parameters are allowed.

    :param allowed_optional_pars: list of allowed optional parameters.
    :param pars: list of passed parameters.
    """
    for key, item in pars.items():
        if not is_parameter_allowed(key, allowed_optional_pars):
            raise UnknownOptionalParameter(f"Unknown parameter: '{key}'")


def is_parameter_allowed(parameter, list_of_allowed_parameters):
    """Check if parameters is in list."""
    return parameter in list_of_allowed_parameters


def parse_text_response_to_format(response, parse_format=Format.DICT):
    """Parse response of request to parse_format.

    :param response: request response.
    :param parse_format: desired format.
    :return: response in desired format.
    """
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
