from src.WeatherStationClient.WeatherStationMeasurementsClient.Measurement.Measurment import MeasurementCloudsDetails, \
    MeasurementWeatherDetails, StationMeasurement


class MeasurmentToDictConverter:

    @staticmethod
    def clouds_measurements_to_dict(cloud_measurment: MeasurementCloudsDetails):
        cloud_details_dict = {key: val for key, val in cloud_measurment.__dict__.items() if val}
        return cloud_details_dict

    @staticmethod
    def weather_details_to_dict(measurment_details: MeasurementWeatherDetails):
        weather_details_dict = {key: val for key, val in measurment_details.__dict__.items() if val}
        return weather_details_dict

    @staticmethod
    def station_measurement_to_dict(measurement: StationMeasurement):
        station_measurement_dict = {}
        for key, val in measurement.__dict__.items():
            if val:
                if key == "clouds":
                    if isinstance(val, list):
                        cloud_dict_array = []
                        for cloud in val:
                            cloud_dict_array.append(MeasurmentToDictConverter.weather_details_to_dict(val))
                        station_measurement_dict["clouds"] = cloud_dict_array
                    else:
                        station_measurement_dict["clouds"] = [MeasurmentToDictConverter.weather_details_to_dict(val)]
                elif key == "weather":
                    if isinstance(val, list):
                        weather_dict_array = []
                        for weather in val:
                            weather_dict_array.append(MeasurmentToDictConverter.weather_details_to_dict(val))
                        station_measurement_dict["weather"] = weather_dict_array
                    else:
                        station_measurement_dict["weather"] = [MeasurmentToDictConverter.weather_details_to_dict(val)]

        return station_measurement_dict
