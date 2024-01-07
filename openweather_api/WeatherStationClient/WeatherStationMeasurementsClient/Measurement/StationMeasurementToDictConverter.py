from openweather_api.WeatherStationClient.WeatherStationMeasurementsClient.Measurement.StastionMeasurment import StationMeasurementCloudsDetails, \
    StationMeasurementWeatherDetails, StationMeasurement


class StationMeasurementToDictConverter:
    """Convert particular measurement data structures to dictionary."""
    @staticmethod
    def clouds_measurements_to_dict(cloud_measurement: StationMeasurementCloudsDetails):
        """Convert Cloud measurement data to dictionary.

        :param cloud_measurement: Cloud measurement data structure
        :return: dictionary contains cloud measurement
        """
        cloud_details_dict = {key: val for key, val in cloud_measurement.__dict__.items() if val}
        return cloud_details_dict

    @staticmethod
    def weather_details_to_dict(measurement_details: StationMeasurementWeatherDetails):
        """Convert Weather details measurement data to dictionary.

        :param measurement_details: Weather details data structure.
        :return: dictionary contains weather details.
        """
        weather_details_dict = {key: val for key, val in measurement_details.__dict__.items() if val}
        return weather_details_dict

    @staticmethod
    def station_measurement_to_dict(measurement: StationMeasurement):
        """Convert whole measurement data to dictionary.

        :param measurement: Station measurement data structure.
        :return: dictionary contains station measurement.
        """
        station_measurement_dict = {}
        for key, val in measurement.__dict__.items():
            if val:
                if key == "clouds":
                    if isinstance(val, list):
                        cloud_dict_array = []
                        for cloud in val:
                            cloud_dict_array.append(StationMeasurementToDictConverter.weather_details_to_dict(val))
                        station_measurement_dict["clouds"] = cloud_dict_array
                    else:
                        station_measurement_dict["clouds"] = [StationMeasurementToDictConverter.weather_details_to_dict(val)]
                elif key == "weather":
                    if isinstance(val, list):
                        weather_dict_array = []
                        for weather in val:
                            weather_dict_array.append(StationMeasurementToDictConverter.weather_details_to_dict(val))
                        station_measurement_dict["weather"] = weather_dict_array
                    else:
                        station_measurement_dict["weather"] = [StationMeasurementToDictConverter.weather_details_to_dict(val)]

        return station_measurement_dict
