from dataclasses import dataclass
from src.WeatherTriggers.Triggers.IToDict import IToDict


@dataclass
class CoordinatesPoint:
    lat: float
    lon: float


class BaseTriggerArea:

    def __init__(self, area_type, coordinates):
        self.area_type = area_type
        self.coordinates = coordinates


@dataclass
class PointTriggerArea(IToDict, BaseTriggerArea):

    def __init__(self, coordinates):
        super().__init__("Point", coordinates)

    def toDict(self) -> dict:
        point_trigger_dict = {
            "type": self.area_type,
            "coordinates": [
                self.coordinates.lat,
                self.coordinates.lon
            ]
        }
        return [point_trigger_dict]


@dataclass
class MultiPointTriggerArea(IToDict, BaseTriggerArea):

    def __init__(self, coordinates):
        super().__init__(area_type="MultiPoint", coordinates=coordinates)

    def toDict(self) -> dict:
        # TO DO
        pass


@dataclass
class PolygonTriggerArea(IToDict, BaseTriggerArea):

    def __init__(self, coordinates):
        super().__init__(area_type="Polygon", coordinates=coordinates)

    def toDict(self) -> dict:
        # TO DO
        pass


@dataclass
class MultiPolygonTriggerArea(IToDict, BaseTriggerArea):

    def __init__(self, coordinates):
        super().__init__(area_type="MultiPolygon", coordinates=coordinates)

    def toDict(self) -> dict:
        # TO DO
        pass
