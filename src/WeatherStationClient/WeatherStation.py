import json
import requests


class RegisteredStation:

    def __init__(self, external_id=None, name=None, latitude=None, longitude=None, altitude=None):
        self.external_id = external_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude


class Station:

    _UPDATE_STATION_INFO = "http://api.openweathermap.org/data/3.0/stations/{station_id}?appid={api_key}"
    _DELETE_STATION = "http://api.openweathermap.org/data/3.0/stations/{station_id}?appid={api_key}"
    _SEND_MEASUREMENT = "http://api.openweathermap.org/data/3.0/measurements?appid={api_key}"
    _GET_MEASUREMENT = "http://api.openweathermap.org/data/3.0/measurements?appid={api_key}&station_id={station_id}&type={type}&limit={limit}&from={from_dt}&to={to_dt}"
    _POST_HEADERS = {'Content-Type': 'application/json'}

    def __init__(self, station_info, api_client):
        self.station_info = station_info
        self._api_client = api_client

    def send_measurement(self, station_measurments):
        http_request = self._SEND_MEASUREMENT.format(
            api_key=self._api_client.api_key
        )
        measurments_array_dict = []
        for measurment in station_measurments:
            measurments_array_dict.append(measurment.toDict())
        try:
            response = requests.post(http_request, data=json.dumps(measurments_array_dict, indent=2), headers=self._POST_HEADERS)
        except:
            raise "Error while requesting for list of all stations"
        response = self._api_client._parse_response(response)
        return response

    def get_measurement(self, type, limit, from_dt, to_dt):
        http_request = self._GET_MEASUREMENT.format(
            api_key=self._api_client.api_key,
            station_id=self.station_info["ID"],
            type=type,
            limit=limit,
            from_dt=from_dt,
            to_dt=to_dt
        )
        try:
            response = requests.get(http_request)
        except:
            raise "Error while requesting for list of all stations"
        response = self._api_client._parse_response(response)
        return response

    def update_station(self, register_station: RegisteredStation = None):
        http_request = self._UPDATE_STATION_INFO.format(
            station_id=self.station_info["ID"],
            api_key=self._api_client.api_key
        )
        try:
            response = requests.put(
                http_request,
                data=self.register_station.__dict__ or self._create_register_station(),
                headers=self._POST_HEADERS
            )
        except:
            raise "Error while requesting for update information about station "
        response = self._api_client._parse_response(response)
        return response

    def delete_station(self):
        http_request = self._DELETE_STATION.format(
            station_id=self.station_info["ID"],
            api_key=self._api_client._api_key
        )
        try:
            response = requests.delete(http_request)
        except:
            raise "Error while requesting for update information about station "
        response = self._api_client._parse_response(response)
        #self.station_info = {}
        return response

    def _create_register_station(self):
        return RegisteredStation(
            external_id=self.station_info["external_id"],
            name=self.station_info["name"],
            altitude=self.station_info["latitude"],
            latitude=self.station_info["longitude"],
            longitude=self.station_info["altitude"]
        )