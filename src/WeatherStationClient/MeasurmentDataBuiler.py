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

    def remove_measurement(self, measurement):
        try:
            self._measurements.remove(measurement)
        except Exception as e:
            raise Exception(e)

        return self

    def clear_measurements(self):
        self._measurements.clear()

    def build(self):
        measurements_data = []
        for measurement in self._measurements:
            dict_measurement = measurement.toDict()
            self._add_station_id_to_measurement_data(dict_measurement)
            measurements_data.append(dict_measurement)
        return measurements_data

    def _add_station_id_to_measurement_data(self, measurement):
        measurement["station_id"] = self.station_id
