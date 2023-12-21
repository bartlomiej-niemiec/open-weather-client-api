from dataclasses import dataclass
from enum import IntEnum


class ZoomCoordinatesLowerBound:
    Worldwide = 0
    OneQuarterOfTheWorld = 0
    Subcontinental = 0
    LargestCountry = 0
    LargestAsiaCountry = 0
    LargeAfricanCountry = 0
    LargeEuropeanCountry = 0
    SmallCountry = 0
    LargeMetropolitan = 0
    Metropolitan = 0


class ZoomCoordinatesUpperBound:
    Worldwide = 1
    OneQuarterOfTheWorld = 1
    Subcontinental = 3
    LargestCountry = 7
    LargestAsiaCountry = 15
    LargeAfricanCountry = 31
    LargeEuropeanCountry = 63
    SmallCountry = 127
    LargeMetropolitan = 255
    Metropolitan = 511


class MapZoom(IntEnum):
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
