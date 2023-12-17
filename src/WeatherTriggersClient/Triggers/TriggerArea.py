from dataclasses import dataclass


@dataclass
class CoordinatesPoint:
    lat: float
    lon: float


class BaseTriggerArea:

    def __init__(self, area_type, coordinates):
        self.area_type = area_type
        self.coordinates = coordinates


@dataclass
class PointTriggerArea(BaseTriggerArea):

    def __init__(self, coordinates):
        super().__init__("Point", coordinates)


@dataclass
class MultiPointTriggerArea(BaseTriggerArea):

    def __init__(self, coordinates):
        super().__init__(area_type="MultiPoint", coordinates=coordinates)


@dataclass
class PolygonTriggerArea(BaseTriggerArea):

    def __init__(self, coordinates):
        super().__init__(area_type="Polygon", coordinates=coordinates)


@dataclass
class MultiPolygonTriggerArea(BaseTriggerArea):

    def __init__(self, coordinates):
        super().__init__(area_type="MultiPolygon", coordinates=coordinates)
