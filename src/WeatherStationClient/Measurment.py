from dataclasses import dataclass


@dataclass
class MeasurementCloudsDetails:
    distance: int = None  # m
    condition: str = None  # SKC, NSC, FEW, SCT, BKN, OVC
    cumulus: str = None  # CB, TCU


@dataclass
class MeasurementWeatherDetails:
    precipitation: str = None  # Additional description, METAR
    descriptor: str = None  # Additional description, METAR
    intensity: str = None  # Additional description, METAR
    proximity: str = None  # Additional description, METAR
    obscuration: str = None  # Additional description, METAR
    other: str = None  # Additional description, METAR


@dataclass
class StationMeasurement:
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