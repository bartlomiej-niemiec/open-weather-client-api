from abc import ABC, abstractmethod
from dataclasses import dataclass


class MeasurementData(ABC):

    @abstractmethod
    def toDict(self) -> dict:
        pass


@dataclass
class MeasurementCloudsDetails(MeasurementData):
    distance: int = None  # m
    condition: str = None  # SKC, NSC, FEW, SCT, BKN, OVC
    cumulus: str = None  # CB, TCU

    def toDict(self):
        cloud_details_dict = {key: val for key, val in self.__dict__.items() if val}
        return cloud_details_dict


@dataclass
class MeasurementWeatherDetails(MeasurementData):
    precipitation: str = None  # Additional description, METAR
    descriptor: str = None  # Additional description, METAR
    intensity: str = None  # Additional description, METAR
    proximity: str = None  # Additional description, METAR
    obscuration: str = None  # Additional description, METAR
    other: str = None  # Additional description, METAR

    def toDict(self):
        weather_details_dict = {key: val for key, val in self.__dict__.items() if val}
        return weather_details_dict


@dataclass
class StationMeasurement(MeasurementData):
    dt: str = None  # Unix time
    temperature: float = None  # Celsius
    wind_speed: float = None  # m/s
    wind_gust: float = None  # m/s
    wind_deg: float = None  # Degrees from 0 to 360
    pressure: float = None  # Hectopascal
    humidity: float = None  # %
    rain_1h: float = None  # mm
    rain_6h: float = None  # mm
    rain_24h: float = None  # mm
    snow_1h: float = None  # mm
    snow_6h: float = None  # mm
    snow_24h: float = None  # mm
    dew_point: float = None  # mm
    humidex: float = None  # Celsius
    heat_index: float = None  # Celsius
    visibility_distance: float = None  # km
    visibility_prefix: str = None  # N, E, S, W
    clouds: MeasurementCloudsDetails = None
    weather: MeasurementWeatherDetails = None

    def toDict(self):
        station_measurement_dict = {}
        for key, val in self.__dict__.items():
            if val:
                if key == "clouds" and val is not None:
                    if isinstance(val, list):
                        cloud_dict_array = []
                        for cloud in val:
                            cloud_dict_array.append(cloud.toDict())
                        station_measurement_dict["clouds"] = cloud_dict_array
                    else:
                        station_measurement_dict["clouds"] = [val.toDict()]
                elif key == "weather" and val is not None:
                    if isinstance(val, list):
                        weather_dict_array = []
                        for weather in val:
                            weather_dict_array.append(weather.toDict())
                        station_measurement_dict["weather"] = weather_dict_array
                    else:
                        station_measurement_dict["weather"] = [val.toDict()]

        return station_measurement_dict
