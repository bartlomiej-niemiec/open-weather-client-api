from typing import List
from src.GenericClient._utils import parse_text_response
from src.GenericClient.base_client import Client
from src.WeatherStationClient.Measurment import StationMeasurement
from src.WeatherStationClient.MeasurmentDataBuiler import StationMeasurementDataBuilder


class WeatherStationMeasurement(Client):
    _API_URL = "http://api.openweathermap.org/data/3.0/measurements"

    def __init__(self, station_id, api_key):
        super().__init__(api_key)
        self.station_id = station_id

    def send_measurement(self, measurements: List[StationMeasurement]):
        post_request_response = self._request(
            'POST',
            url=self._API_URL,
            data=convert_measurements_to_request_data(measurements, self.station_id)
        )
        response = parse_text_response(post_request_response)
        return response

    def get_measurement(self, type, limit, from_dt, to_dt):
        _get_req_params = {
            "type": type,
            "station_id": self.station_id['id'],
            "limit": limit,
            "from": from_dt,
            "to": to_dt
        }
        get_request_response = self._request(
            'GET',
            url=self._API_URL,
            data=_get_req_params
        )
        measurements = parse_text_response(get_request_response)
        return measurements


def convert_measurements_to_request_data(measurements, station_id):
    builder = StationMeasurementDataBuilder(station_id)
    return builder.add_measurement(measurements).build()
