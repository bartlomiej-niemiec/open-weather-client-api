from src.GenericClient.base_client import Client, parse_response
from src.WeatherStationClient.StationParameters import StationParameters


class WeatherStationMeasurement(Client):
    _API_URL = "http://api.openweathermap.org/data/3.0/measurements"

    def __init__(self, station_parameters: StationParameters, api_key):
        super().__init__(api_key)
        self._station_parameters = station_parameters

    def send_measurement(self, station_measurements):
        measurements_array_dict = [measurement.toDict() for measurement in station_measurements]
        post_request_response = self._post_request(
            url=self._API_URL,
            data=measurements_array_dict
        )
        response = parse_response(post_request_response)
        return response

    def get_measurement(self, type, limit, from_dt, to_dt):
        _get_req_params = {
            "type": type,
            "station_id": self._station_parameters['id'],
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

    def get_station_parameters(self):
        return self._station_parameters

    def set_station_parameters(self, station_parameters: StationParameters):
        self._station_parameters = station_parameters
