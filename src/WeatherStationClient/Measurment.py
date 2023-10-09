from dataclasses import dataclass
from src._utils import UnixTime

@dataclass
class MeasurementCloudsDetails:
    distance: int = None
    condition: str = None
    cumulus: str = None

@dataclass
class MeasurementWeatherDetails:
    precipitation: str = None
    descriptor: str = None
    intensity: str = None
    proximity: str = None
    obscuration: str = None
    other: str = None

@dataclass
class StationMeasurement:

    def __init__(self):
        station_id: str = None
        dt: UnixTime = UnixTime(year=0, month=0, day=0)
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
        clouds: MeasurementCloudsDetails
        weather: MeasurementWeatherDetails
