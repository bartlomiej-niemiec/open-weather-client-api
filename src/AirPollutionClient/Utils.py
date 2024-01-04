from datetime import datetime
from enum import IntEnum

from src.GenericClient.Utils import parse_text_response


def convert_timestamp_date_string(unix_timestamp):
    """Convert timestamp to UTC date. 

    Args:
        unix_timestamp int: Unix Time

    Returns:
        str: date
    """
    return datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')


def replace_unix_dt_with_date_string(request_response):
    """Replace Unix DT field with date string.

    Args:
        request_response : Request.Response from AirPollution

    Returns:
        Request.Response: response with replaced 'dt' field.
    """
    for item in request_response['list']:
        if timestamp := item.get('dt'):
            item['dt'] = convert_timestamp_date_string(timestamp)
    return request_response


def process_air_polution_response(request_response):
    """Process AirPollution API response.

    Args:
        request_response Request.Response: response from air pollution api.

    Returns:
        dict: air polution data with replaced 'dt' field.
    """
    dict_response = parse_text_response(request_response)
    dict_response['timezone'] = 'UTC'
    dict_response = replace_unix_dt_with_date_string(dict_response)
    return dict_response


class AirPollutionUrls(IntEnum):
    current = 0
    forecast = 1
    historical = 2