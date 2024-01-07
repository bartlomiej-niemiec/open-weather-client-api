from abc import ABC
from dataclasses import dataclass
from typing import List
from src.openweather_api.WeatherTriggersClient.Triggers.Exceptions import NotClosedPolygon


@dataclass
class CoordinatesPoint:
    lat: float
    lon: float


class BaseTriggerArea(ABC):

    def __init__(self, area_type, points):
        self.area_type = area_type
        self.points = points

    def _is_point_valid(self, point):
        return isinstance(point, CoordinatesPoint)

    def _raise_point_type_error(self):
        TypeError("point parameter should be type of CoordinatesPoint")


class PointTriggerArea(BaseTriggerArea):

    def __init__(self, point: CoordinatesPoint):
        if not self._is_point_valid(point):
            self._raise_point_type_error()
        super().__init__("Point", point)


class MultiPointTriggerArea(BaseTriggerArea):

    def __init__(self):
        super().__init__(area_type="MultiPoint", points=[])

    def add_point(self, point):
        if not self._is_point_valid(point):
            self._raise_point_type_error()
        self.points.append(point)
        return self

    def add_points_list(self, points: List[CoordinatesPoint]):
        self.points.extend(points)
        return self

    def remove_point(self, point):
        self.points.remove(point)
        return self


class PolygonTriggerArea(BaseTriggerArea):

    def __init__(self, polygon: List[CoordinatesPoint]):
        if not self._is_polygon_closed(polygon):
            raise NotClosedPolygon("Provide Closed Polygon")
        super().__init__(area_type="Polygon", points=polygon)

    def _is_polygon_closed(self, polygon):
        return (polygon[0].lat == polygon[-1].lat) and (polygon[0].lon == polygon[-1].lon)


class MultiPolygonTriggerArea(BaseTriggerArea):

    def __init__(self):
        super().__init__(area_type="MultiPolygon", points=[])

    def add_polygon(self, polygon: PolygonTriggerArea):
        self.points.append(polygon)
        return self

    def _is_polygon_closed(self, polygon):
        return (polygon[0].lat == polygon[-1].lat) and (polygon[0].lon == polygon[-1].lon)
