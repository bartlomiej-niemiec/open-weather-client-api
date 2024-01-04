from src.WeatherStationClient.WeatherStationMeasurements.MeasurmentToDictConverter import MeasurmentToDictConverter


class StationMeasurementDataBuilder:

    def __init__(self, station_id):
        self._measurements = []
        self.station_id = station_id

    def add_measurement(self, measurement):
        if isinstance(measurement, list):
            self._measurements.extend(measurement)
        else:
            self._measurements.append(measurement)
        return self

    def build(self):
        measurements_data = []
        for measurement in self._measurements:
            measurement_data = MeasurmentToDictConverter.station_measurement_to_dict(measurement)
            self._add_station_id_to_measurement_data(measurement_data)
            measurements_data.append(measurement_data)
        return measurements_data

    def _add_station_id_to_measurement_data(self, measurement):
        measurement["station_id"] = self.station_id
