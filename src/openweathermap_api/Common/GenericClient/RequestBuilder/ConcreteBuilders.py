from src.openweathermap_api.Common.GenericClient.Constants import APPID_PARAM_NAME, POST_REQ_HEADERS
from src.openweathermap_api.Common.GenericClient.RequestBuilder.RequestBuilder import RequestBuilder


class GetAndDeleteRequestBuilder(RequestBuilder):

    """OpenWeather GET and Delete request builder."""

    def build_headers(self, headers):
        self._request.headers = None

    def build_data(self, data: dict):
        _data = data.copy()
        _data[APPID_PARAM_NAME] = self._api_key
        self._request.params = _data

    def build_url(self, url):
        self._request.url = url


class PostAndPutRequestBuilder(RequestBuilder):

    """OpenWeather POST and PUT request builder."""

    def build_headers(self, headers):
        self._request.headers = POST_REQ_HEADERS

    def build_data(self, data: dict):
        self._request.json = data

    def build_url(self, url):
        url += f"?{APPID_PARAM_NAME}={self._api_key}"
        self._request.url = url
