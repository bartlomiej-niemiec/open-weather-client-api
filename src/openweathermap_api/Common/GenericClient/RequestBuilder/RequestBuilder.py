from abc import ABC, abstractmethod
from requests import Request


class RequestBuilder(ABC):

    """Custom request builder interface."""

    def __init__(self, api_key):
        """Init.

        :param api_key: OpenWeather API key.
        """
        self._request = Request()
        self._api_key = api_key

    def build_req_type(self, req_type):
        """Add/Build desired request type (GET e.g) to request.

        :param req_type: request type.
        """
        self._request.method = req_type

    @abstractmethod
    def build_headers(self, headers):
        """Add/Build desired request type (GET e.g) to request.

        :param headers: request header.
        """
        pass

    @abstractmethod
    def build_data(self, data):
        """Add/Build data to request.

        :param data: payload to request.
        :return:
        """
        pass

    @abstractmethod
    def build_url(self, url):
        """Add/Build URL address to request.

        :param url: set url address of request.
        :return:
        """
        pass

    def get_and_finish_build(self):
        """Prepare request.

        :return: prepared request.
        """
        prepared_request = self._request.prepare()
        self._request = Request()
        return prepared_request


