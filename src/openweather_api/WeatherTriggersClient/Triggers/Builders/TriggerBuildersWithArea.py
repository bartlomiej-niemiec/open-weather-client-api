from src.openweather_api.WeatherTriggersClient.Triggers.Builders.CommonTriggerBuilderWithoutArea import CommonBuilderWithoutArea
from src.openweather_api.WeatherTriggersClient.Triggers.TriggerArea import BaseTriggerArea


class PointTriggerBuilder(CommonBuilderWithoutArea):

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


class MultiPointTriggerBuilder(CommonBuilderWithoutArea):

    def build_area(self, area: BaseTriggerArea):
        coordinates = [[point.lat, point.lon] for point in area.points]
        self._data_build["build_area"] = [
            {
                "type": area.area_type,
                "coordinates": coordinates
            }
        ]


class PolygonTriggerBuilder(CommonBuilderWithoutArea):

    def build_area(self, area: BaseTriggerArea):
        coordinates = [[point.lat, point.lon] for point in area.points]
        self._data_build["build_area"] = [
            {
                "type": area.area_type,
                "coordinates": [coordinates]
            }
        ]


class MultiPolygonTriggerBuilder(CommonBuilderWithoutArea):
    def build_area(self, area: BaseTriggerArea):
        coordinates = [[[point.lat, point.lon] for point in polygon.points] for polygon in area.points]
        self._data_build["build_area"] = [
            {
                "type": area.area_type,
                "coordinates": [coordinates]
            }
        ]
