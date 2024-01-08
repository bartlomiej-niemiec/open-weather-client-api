from src.openweathermap_api.Utils import Format
import json


def parse_request_response_to_format(response, parse_format=Format.DICT):
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
