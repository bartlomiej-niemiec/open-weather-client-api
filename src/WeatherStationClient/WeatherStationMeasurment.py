from src.GenericClient.base_client import Client, parse_response
from src.WeatherStationClient.Measurment import MeasurementData


class WeatherStationMeasurement(Client):
    _API_URL = "http://api.openweathermap.org/data/3.0/measurements"

    def __init__(self, station_id, api_key):
        super().__init__(api_key)
        self.station_id = station_id

    def send_measurement(self, measurements: list[MeasurementData]):
        post_request_response = self._post_request(
            url=self._API_URL,
            data=self._get_measurements_dict_list(measurements)
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

    def _get_measurements_dict_list(self, measurements):
        measurements_dict_list = []
        for measurement in measurements:
            dict_measurement = measurement.toDict()
            self._add_station_id_to_measurement_data(dict_measurement)
            measurements_dict_list.append(dict_measurement)
        return measurements_dict_list

    def _add_station_id_to_measurement_data(self, measurement):
        measurement["station_id"] = self.station_id

