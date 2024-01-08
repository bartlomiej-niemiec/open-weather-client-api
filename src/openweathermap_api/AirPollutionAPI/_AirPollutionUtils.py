from datetime import datetime
from enum import IntEnum
from src.openweathermap_api.Common.GenericClient.RequestResponseParsing import parse_request_response_to_format


def convert_unix_timestamp_to_utc(unix_timestamp):
    """Convert timestamp to UTC timestamp.

    Args:
        unix_timestamp int: Unix Time

    Returns:
        str: date
    """
    return datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')


def replace_unix_timestamp_with_utc_in_request_response(request_response):
    """Replace Unix timestamp field with UTC timestamp.

    Args:
        request_response : Request.Response from AirPollution

    Returns:
        Request.Response: response with replaced 'dt' field.
    """
    for item in request_response['list']:
        if timestamp := item.get('dt'):
            item['dt'] = convert_unix_timestamp_to_utc(timestamp)
    return request_response


def parse_air_polution_response(request_response):
    """Process AirPollution API response.

    Args:
        request_response:  Request.Response from AirPollution.

    Returns:
        dict: air polution data with replaced 'dt' field.
    """
    dict_response = parse_request_response_to_format(request_response)
    dict_response['timezone'] = 'UTC'
    dict_response = replace_unix_timestamp_with_utc_in_request_response(dict_response)
    return dict_response


class AirPollutionUrls(IntEnum):
    current = 0
    forecast = 1
    historical = 2