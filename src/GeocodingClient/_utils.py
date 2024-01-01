from enum import IntEnum


class GeocodingUrls(IntEnum):
    by_location_name = 0
    by_zip_code = 1
    reverse = 2


ALLOWED_OPTIONAL_PARS = ['limit']