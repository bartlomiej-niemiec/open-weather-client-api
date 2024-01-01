from datetime import datetime
from enum import IntEnum

from src.GenericClient._utils import parse_text_response


def convert_timestamp_to_utc_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def replace_dt_timestamp_with_utc(response):
    for item in response['list']:
        if timestamp := item.get('dt'):
            item['dt'] = convert_timestamp_to_utc_date(timestamp)
    return response


def process_air_polution_response(response):
    dict_response = parse_text_response(response)
    dict_response['timezone'] = 'UTC'
    dict_response = replace_dt_timestamp_with_utc(dict_response)
    return dict_response


class AirPollutionUrls(IntEnum):
    current = 0
    forecast = 1
    historical = 2