from dataclasses import dataclass
from src._utils import UnixTime


@dataclass
class MeasurementCloudsDetails:
    distance: int = None
    condition: str = None
    cumulus: str = None

    def toDict(self):
        cloud_details_dict = {}
        for key, val in self.__dict__.items():
            if val:
                cloud_details_dict[key] = val

        return cloud_details_dict


@dataclass
class MeasurementWeatherDetails:
    precipitation: str = None
    descriptor: str = None
    intensity: str = None
    proximity: str = None
    obscuration: str = None
    other: str = None

    def toDict(self):
        weather_details_dict = {}
        for key, val in self.__dict__.items():
            if val:
                weather_details_dict[key] = val

        return weather_details_dict


@dataclass
class StationMeasurement:
    station_id: str = None
    dt: UnixTime = None
    temperature: float = None
    wind_speed: float = None
    wind_gust: float = None
    wind_deg: float = None
    pressure: float = None
    humidity: float = None
    rain_1h: float = None
    rain_6h: float = None
    rain_24h: float = None
    snow_1h: float = None
    snow_6h: float = None
    snow_24h: float = None
    dew_point: float = None
    humidex: float = None
    heat_index: float = None
    visibility_distance: float = None
    visibility_prefix: str = None
    clouds: MeasurementCloudsDetails = None
    weather: MeasurementWeatherDetails = None

    def toDict(self):
        station_measurment_dict = {}
        for key, val in self.__dict__.items():
            if val:
                if key == "clouds" and val is not None:
                    if isinstance(val, list):
                        cloud_dict_array = []
                        for cloud in val:
                            cloud_dict_array.append(cloud.toDict())
                        station_measurment_dict["clouds"] = cloud_dict_array
                    else:
                        station_measurment_dict["clouds"] = [val.toDict()]
                elif key == "weather" and val is not None:
                    if isinstance(val, list):
                        weather_dict_array = []
                        for weather in val:
                            weather_dict_array.append(weather.toDict())
                        station_measurment_dict["weather"] = weather_dict_array
                    else:
                        station_measurment_dict["weather"] = [val.toDict()]
                elif key == "dt" and val is not None:
                    station_measurment_dict["dt"] = int(val)
                else:
                    station_measurment_dict[key] = val

        return station_measurment_dict
