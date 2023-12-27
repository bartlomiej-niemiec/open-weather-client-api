import requests

from src.GenericClient.exceptions import UnknownOptionalParameter
from src.WeatherClient._constants import Format
from src.GenericClient.RequestBuilder import RequestDirector
import json


class Client:
    ALLOWED_OPTIONAL_PARS = []

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._request_director = RequestDirector(api_key)

    def _request(self, req_type, url, data, headers=None, exception=None):
        request_session = requests.Session()
        prepared_request = self._request_director.constructRequest(req_type, url, data, headers)
        try:
            response = request_session.send(prepared_request)
            response.raise_for_status()
        except Exception as exc:
            if exception:
                raise exception(exc)
            else:
                raise Exception(exc)

        return response

    def _add_optional_params_from_kwargs_to_request_params(self, request_params, kwargs):
        optional_args = parse_optional_parameters(
            self.ALLOWED_OPTIONAL_PARS,
            kwargs
        )
        request_params.update(optional_args)


def parse_optional_parameters(allowed_optional_pars, pars):
    optional_args = {}
    for key, item in pars.items():
        if key not in allowed_optional_pars:
            raise UnknownOptionalParameter(f"Unknown parameter: '{key}'")
        else:
            optional_args[key] = item

    return optional_args


def parse_response(response, parse_format=Format.DICT):
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
