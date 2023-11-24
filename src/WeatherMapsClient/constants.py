from dataclasses import dataclass
from enum import IntEnum


class ZoomCoordinatesLowerBound:
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0


class ZoomCoordinatesUpperBound:
    zero = 1
    one = 1
    two = 3
    three = 7
    four = 15
    five = 31
    six = 63
    seven = 127
    eight = 255
    nine = 511


class MapArea(IntEnum):
    Worldwide = 0
    OneQuarterOfTheWorld = 1
    Subcontinental = 2
    LargestCountry = 3
    LargestAsiaCountry = 4
    LargeAfricanCountry = 5
    LargeEuropeanCountry = 6
    SmallCountry = 7
    LargeMetropolitan = 8
    Metropolitan = 9


@dataclass(frozen=True)
class Layers:
    clouds: str = "clouds_new"
    precipitation: str = "precipitation_new"
    sea_level_pressure: str = "pressure_new"
    wind_speed: str = "wind_new"
    temperature: str = "temp_new"
