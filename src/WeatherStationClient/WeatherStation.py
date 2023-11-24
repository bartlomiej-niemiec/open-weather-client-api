import json
import requests
from dataclasses import dataclass
from src.GenericClient.base_client import Client


@dataclass
class RegisterStationParameters:
    external_id: str = None
    name: str = None
    latitude: float = None
    longitude: float = None
    altitude: float = None


class Station(Client):
    _UPDATE_STATION_INFO = "http://api.openweathermap.org/data/3.0/stations/{station_id}?appid={api_key}"
    _DELETE_STATION = "http://api.openweathermap.org/data/3.0/stations/{station_id}?appid={api_key}"
    _SEND_MEASUREMENT = "http://api.openweathermap.org/data/3.0/measurements?appid={api_key}"
    _GET_MEASUREMENT = "http://api.openweathermap.org/data/3.0/measurements?appid={api_key}&station_id={station_id}&type={type}&limit={limit}&from={from_dt}&to={to_dt}"
    _POST_HEADERS = {'Content-Type': 'application/json'}

    def __init__(self, station_parameters: dict, api_key):
        super().__init__(api_key)
        self._station_parameters = station_parameters

    def send_measurement(self, station_measurments):
        http_request = self._SEND_MEASUREMENT.format(
            api_key=self.api_key
        )
        measurments_array_dict = []
        for measurment in station_measurments:
            measurments_array_dict.append(measurment.toDict())
        try:
            response = requests.post(http_request, data=json.dumps(measurments_array_dict, indent=2),
                                     headers=self._POST_HEADERS)
        except:
            raise "Error while requesting for list of all stations"
        response = _parse_response(response)
        return response

    def get_measurement(self, type, limit, from_dt, to_dt):
        http_request = self._GET_MEASUREMENT.format(
            api_key=self.api_key,
            station_id=self.station_parameters.id,
            type=type,
            limit=limit,
            from_dt=from_dt,
            to_dt=to_dt
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for list of all stations"
        response = _parse_response(response)
        return response

    def update_station(self, station_parameters: StationParameters = None):
        http_request = self._UPDATE_STATION_INFO.format(
            station_id=self.station_parameters.id,
            api_key=self.api_key
        )
        try:
            response = requests.put(
                http_request,
                data=station_parameters.__dict__ or self.station_parameters.registration_parameters.__dict__,
                headers=self._POST_HEADERS
            )
        except:
            raise "Error while requesting for update information about station "
        response = _parse_response(response)
        return response

    def delete_station(self):
        http_request = self._DELETE_STATION.format(
            station_id=self.station_parameters.id,
            api_key=self.api_key
        )
        try:
            response = requests.delete(http_request)
        except:
            raise "Error while requesting for update information about station "
        response = _parse_response(response)
        self.station_info = {}
        return response

    def get_station_parameters(self):
        return self._station_parameters
