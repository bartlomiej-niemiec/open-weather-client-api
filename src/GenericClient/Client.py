import requests
from src._open_weather import Format
import json


def parse_optional_parameters(allowed_optional_pars, pars):
    optional_args = {}
    for key, item in pars.items():
        if key not in allowed_optional_pars:
            raise UnknownOptionalParameter(f"Unknown parameter: '{key}'")
        else:
            optional_args[key] = item

    return optional_args


class UnknownOptionalParameter(Exception):
    pass


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


class Client:
    _APPID_PARAM_NAME = "appid"
    _POST_REQ_HEADERS = {'Content-Type': 'application/json'}
    ALLOWED_OPTIONAL_PARS = []

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._get_params_dict: dict = {}
        self._post_data_dict: dict = {}

    def _get_request(self, url):
        self._get_params_dict[self._APPID_PARAM_NAME] = self.api_key
        try:
            response = requests.get(
                url=url,
                params=self._get_params_dict
            )
            response.raise_for_status()
        except Exception as exc:
            raise GetRequestError(exc)

        return response

    def _post_request(self, url):
        self._post_data_dict[self._APPID_PARAM_NAME] = self.api_key
        try:
            response = requests.post(
                url=url,
                data=self._post_data_dict,
                headers=self._POST_REQ_HEADERS
            )
            response.raise_for_status()
        except Exception as exc:
            raise PostRequestError(exc)
        return response

    def _add_optional_params_from_kwargs_to_request_params(self, kwargs):
        optional_args = parse_optional_parameters(
            self.ALLOWED_OPTIONAL_PARS,
            kwargs
        )
        self._get_params_dict.update(optional_args)


class GetRequestError(Exception):
    pass


class PostRequestError(Exception):
    pass
