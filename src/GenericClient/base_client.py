import requests
from src.GenericClient._utils import parse_optional_parameters

from src.GenericClient.RequestBuilder import RequestDirector


class Client:

    def __init__(self, api_key: str):
        self.api_key = api_key
        self._request_director = RequestDirector(api_key)
        self._allowed_optional_pras = []

    def _request(self, req_type, url, data, headers=None, exception=None):
        request_session = requests.Session()
        prepared_request = self._request_director.build_request(req_type, url, data, headers)
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
            self._allowed_optional_pras,
            kwargs
        )
        request_params.update(optional_args)
