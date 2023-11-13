import requests
from abc import ABC, abstractmethod
from src._open_weather import Format
import json


class UnknownOptionalParameter(Exception):
    pass


def parse_optional_parameters(allowed_optional_pars, pars):
    optional_args = {}
    for key, item in pars.items():
        if key not in allowed_optional_pars:
            raise UnknownOptionalParameter(f"Unknown parameter: '{key}'")
        else:
            optional_args[key] = item

    return optional_args


def merge_dicts(dict_1: dict, dict_2: dict) -> dict:
    dict_1_copy = dict_1.copy()
    dict_1_copy.update(dict_2)
    return dict_1_copy


def parse_response(response, parse_format=Format.DICT):
    text_response = response.text
    if text_response:
        parsed_response = None
        if parse_format == Format.DICT:
            parsed_response = json.loads(text_response)
        elif parse_format == Format.JSON:
            parsed_response = response.json()
        elif parse_format == Format.XML:
            pass
        return parsed_response


class Client(ABC):
    _APPID_PARAM_NAME = "appid"
    _POST_REQ_HEADERS = {'Content-Type': 'application/json'}

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._get_params_dict = None
        self._post_data_dict = None

    def _get_request(self, non_default_url=None):
        self._get_params_dict[self._APPID_PARAM_NAME] = self.api_key
        response = requests.get(
            url=non_default_url or self._get_api_url(),
            params=self._get_params_dict
        )
        return response

    def _post_request(self, non_default_url=None):
        self._post_data_dict[self._APPID_PARAM_NAME] = self.api_key
        response = requests.post(
            url=non_default_url or self._get_api_url(),
            data=self._post_data_dict,
            headers=self._POST_REQ_HEADERS
        )
        return response

    @abstractmethod
    def _get_api_url(self) -> str:
        empty_str = ""
        return empty_str
