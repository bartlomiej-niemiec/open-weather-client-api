from src.GenericClient.base_client import Client, parse_response
from src.WeatherStationClient.Measurment import StationMeasurement
from src.WeatherStationClient.MeasurmentDataBuiler import StationMeasurementDataBuilder


def _get_measurements_data_list(measurements):
    builder = StationMeasurementDataBuilder()
    for measurement in measurements:
        StationMeasurementDataBuilder.add_measurement(measurement)
    return builder.build()


class WeatherStationMeasurement(Client):
    _API_URL = "http://api.openweathermap.org/data/3.0/measurements"

    def __init__(self, station_id, api_key):
        super().__init__(api_key)
        self.station_id = station_id

    def send_measurement(self, measurements):
        post_request_response = self._post_request(
            url=self._API_URL,
            data=_get_measurements_data_list(measurements)
        )
        response = parse_response(post_request_response)
        return response

    def get_measurement(self, type, limit, from_dt, to_dt):
        _get_req_params = {
            "type": type,
            "station_id": self.station_id['id'],
            "limit": limit,
            "from": from_dt,
            "to": to_dt
        }
        get_request_response = self._get_request(
            url=self._API_URL,
            params=_get_req_params
        )
        measurements = parse_response(get_request_response)
        return measurements
