from abc import ABC, abstractmethod
from requests import Request
from src.GenericClient.constants import APPID_PARAM_NAME, POST_REQ_HEADERS


class RequestDirector:

    def __init__(self, api_key):
        self._api_key = api_key
        self._get_and_delete_builder = GetAndDeleteRequestBuilder(api_key)
        self._post_and_put_builder = PostAndPutRequestBuilder(api_key)

    def constructRequest(self, req_type, url, data, headers):
        prepared_request = None
        if req_type == "POST" or req_type == "PUT":
            prepared_request = self._common_construct(self._post_and_put_builder, req_type, url, data, headers)
        elif req_type == "DELETE" or req_type == "GET":
            prepared_request = self._common_construct(self._get_and_delete_builder, req_type, url, data, headers)
        else:
            raise Exception("Wrong Request")

        return prepared_request

    def _common_construct(self, builder, req_type, url, data, headers):
        builder.build_req_type(req_type)
        builder.build_headers(headers)
        builder.build_url(url)
        builder.build_data(data)
        return builder.getAndFinishBuild()


class RequestBuilder(ABC):

    def __init__(self, api_key):
        self._request = Request()
        self._api_key = api_key

    def build_req_type(self, req_type):
        self._request.method = req_type

    @abstractmethod
    def build_headers(self, headers):
        pass

    @abstractmethod
    def build_data(self, data):
        pass

    @abstractmethod
    def build_url(self, url):
        pass

    def getAndFinishBuild(self):
        prepared_request = self._request.prepare()
        self._request = Request()
        return prepared_request


class GetAndDeleteRequestBuilder(RequestBuilder):

    def build_headers(self, headers):
        self._request.headers = None

    def build_data(self, data: dict):
        _data = data.copy()
        _data[APPID_PARAM_NAME] = self._api_key
        self._request.data = _data

    def build_url(self, url):
        self._request.url = url


class PostAndPutRequestBuilder(RequestBuilder):

    def build_headers(self, headers):
        self._request.headers = POST_REQ_HEADERS

    def build_data(self, data: dict):
        self._request.json = data

    def build_url(self, url):
        url += f"?{APPID_PARAM_NAME}={self._api_key}"
        self._request.url = url
