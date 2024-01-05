from src.WeatherTriggersClient.Triggers.Builders.GenericTriggerBuilderWithoutArea import GenericBuilderWithoutArea
from src.WeatherTriggersClient.Triggers.TriggerArea import BaseTriggerArea


class PointTriggerBuilder(GenericBuilderWithoutArea):

    def build_area(self, area: BaseTriggerArea):
        self._data_build["build_area"] = [
            {
                "type": area.area_type,
                "coordinates": [
                    area.points.lat,
                    area.points.lon
                ]
            }
        ]


class MultiPointTriggerBuilder(GenericBuilderWithoutArea):

    def build_area(self, area: BaseTriggerArea):
        coordinates = [[point.lat, point.lon] for point in area.points]
        self._data_build["build_area"] = [
            {
                "type": area.area_type,
                "coordinates": coordinates
            }
        ]


class PolygonTriggerBuilder(GenericBuilderWithoutArea):

    def build_area(self, area: BaseTriggerArea):
        coordinates = [[point.lat, point.lon] for point in area.points]
        self._data_build["build_area"] = [
            {
                "type": area.area_type,
                "coordinates": [coordinates]
            }
        ]


class MultiPolygonTriggerBuilder(GenericBuilderWithoutArea):
    def build_area(self, area: BaseTriggerArea):
        coordinates = [[[point.lat, point.lon] for point in polygon.points] for polygon in area.points]
        self._data_build["build_area"] = [
            {
                "type": area.area_type,
                "coordinates": [coordinates]
            }
        ]
