from src.openweather_api.Common.GenericClient.Exceptions import WrongRequestType
from src.openweather_api.Common.GenericClient.RequestBuilder.ConcreteBuilders import GetAndDeleteRequestBuilder, PostAndPutRequestBuilder


class RequestDirector:
    """Management of building process."""

    def __init__(self, api_key):
        """Init.

        :param api_key: OpenWeather API key.
        """
        self._api_key = api_key
        self._get_and_delete_builder = GetAndDeleteRequestBuilder(api_key)
        self._post_and_put_builder = PostAndPutRequestBuilder(api_key)

    def build_request(self, req_type, url, data, headers):
        """ build request with passed parameters.

        :param req_type: request type.
        :param url: set url address of request.
        :param data: payload to request.
        :param headers: request header.
        :return: builded request.
        """

        prepared_request = None
        if req_type == "POST" or req_type == "PUT":
            prepared_request = self._common_request_build(self._post_and_put_builder, req_type, url, data, headers)
        elif req_type == "DELETE" or req_type == "GET":
            prepared_request = self._common_request_build(self._get_and_delete_builder, req_type, url, data, headers)
        else:
            raise WrongRequestType(f"Wrong '{req_type}' request")

        return prepared_request

    def _common_request_build(self, builder, req_type, url, data, headers):
        builder.build_req_type(req_type)
        builder.build_headers(headers)
        builder.build_url(url)
        builder.build_data(data)
        return builder.getAndFinishBuild()
