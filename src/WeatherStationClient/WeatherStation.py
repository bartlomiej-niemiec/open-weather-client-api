import json
from _utils import _check_range, _check_type, _raise_type_exception, _raise_range_exception


def create_station_from_json(jsonString):
    return json.loads(jsonString)


class Station:
    _MAX_LATITUDE = 90
    _MIN_LATITUDE = -90
    _MAX_LONGITUDE = 180
    _MIN_LONGITUDE = -180

    def __init__(self, external_id=None, name=None, latitude=None, longitude=None, altitude=None):
        self._external_id = external_id
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
        self._altitude = altitude

    def toJSON(self):
        station_dict = {
            'external_id': self._external_id,
            'name': self._name,
            'latitude': self._latitude,
            'longitude': self._longitude,
            'altitude': self._altitude,
        }
        return json.dumps(station_dict)

    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, id: str):
        if not _check_type(id, str):
            _raise_type_exception(id, str)
        self._external_id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not _check_type(name, str):
            _raise_type_exception(name, str)
        self._name = name

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        if not _check_type(latitude, float):
            if _check_type(latitude, int):
                latitude = float(latitude)
            else:
                _raise_type_exception(latitude, float)
        if not _check_range(self._MIN_LATITUDE, self._MAX_LATITUDE, latitude):
            _raise_range_exception(self._MIN_LATITUDE, self._MAX_LATITUDE)
        self._latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        if not _check_type(longitude, float):
            if _check_type(longitude, int):
                longitude = float(longitude)
            else:
                _raise_type_exception(longitude, float)
        if not _check_range(self._MIN_LONGITUDE, self._MAX_LONGITUDE, longitude):
            _raise_range_exception(self._MIN_LONGITUDE, self._MAX_LONGITUDE)
        self._longitude = longitude

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, altitude):
        if not _check_type(altitude, float):
            if _check_type(altitude, int):
                altitude = float(altitude)
            else:
                _raise_type_exception(altitude, float)
        self._altitude = altitude
