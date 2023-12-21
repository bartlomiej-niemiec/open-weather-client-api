import requests

from src.GenericClient.exceptions import GetRequestError, PostRequestError, PutRequestError,\
    DeleteRequestError, UnknownOptionalParameter
from src.WeatherClient._constants import Format
import json


class Client:
    _APPID_PARAM_NAME = "appid"
    _POST_REQ_HEADERS = {'Content-Type': 'application/json'}
    ALLOWED_OPTIONAL_PARS = []

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _get_request(self, url: str, params: dict) -> requests.Response:
        params[self._APPID_PARAM_NAME] = self.api_key
        try:
            response = requests.get(
                url=url,
                params=params
            )
            response.raise_for_status()
        except Exception as exc:
            raise GetRequestError(exc)

        return response

    def _delete_request(self, url: str, params: dict) -> requests.Response:
        params[self._APPID_PARAM_NAME] = self.api_key
        try:
            response = requests.delete(
                url=url,
                params=params
            )
            response.raise_for_status()
        except Exception as exc:
            raise DeleteRequestError(exc)

        return response

    def _post_request(self, url: str, data: dict) -> requests.Response:
        url += f"?{self._APPID_PARAM_NAME}={self.api_key}"
        try:
            response = requests.post(
                url=url,
                json=data,
                headers=self._POST_REQ_HEADERS
            )
            response.raise_for_status()
        except Exception as exc:
            raise PostRequestError(exc)
        return response

    def _put_request(self, url: str, data: dict) -> requests.Response:
        url += f"?{self._APPID_PARAM_NAME}={self.api_key}"
        try:
            response = requests.put(
                url=url,
                json=data,
                headers=self._POST_REQ_HEADERS
            )
            response.raise_for_status()
        except Exception as exc:
            raise PutRequestError(exc)
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
