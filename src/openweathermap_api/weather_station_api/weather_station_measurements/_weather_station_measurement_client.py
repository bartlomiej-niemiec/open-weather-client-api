from typing import List
from src.openweathermap_api.common import Client, parse_request_response_to_format
from src.openweathermap_api.weather_station_api.weather_station_measurements.measurement import StationMeasurement, StationMeasurementToDictConverter


class WeatherStationMeasurementClient(Client):
    """Wrapper for OpenWeather Weather Stations API - Measurements."""
    _API_URL = "http://api.openweathermap.org/data/3.0/measurements"

    def __init__(self, station_id, api_key):
        """Initialize object.

        :param station_id: id of registered station.
        :param api_key: OpenWeather API key.
        """
        super().__init__(api_key)
        self.station_id = station_id

    def send_measurement(self, measurements: List[StationMeasurement]):
        """send station measurements.

        :param measurements: list of measurements to send.
        :return: api response.
        """
        post_request_response = self._send_request(
            'POST',
            url=self._API_URL,
            data=convert_measurements_to_request_data(measurements, self.station_id)
        )
        response = parse_request_response_to_format(post_request_response)
        return response

    def get_measurement(self, type, limit, from_dt, to_dt):
        """get measurements that meet criteria.

        :param type: type of the aggregated data.
        :param limit: maximum number of records with the aggregated measurements .
        :param from_dt: the beginning of an interval on which data are requested - Unix Timestamp.
        :param to_dt: The end of an interval on which data are requested - Unix Timestamp.
        :return: api response.
        """
        _get_req_params = {
            "type": type,
            "station_id": self.station_id['id'],
            "limit": limit,
            "from": from_dt,
            "to": to_dt
        }
        get_request_response = self._send_request(
            'GET',
            url=self._API_URL,
            data=_get_req_params
        )
        measurements = parse_request_response_to_format(get_request_response)
        return measurements


def convert_measurements_to_request_data(measurements, station_id):
    """Convert list of measurement data structure to request payload.

    :param measurements: list of station measurements.
    :param station_id: id of station.
    :return: request payload with station measurements data.
    """
    measurements_data = []
    for measurement in measurements:
        measurement_data = StationMeasurementToDictConverter.station_measurement_to_dict(measurement)
        measurement["station_id"] = station_id
        measurements_data.append(measurement_data)
    return measurements_data
