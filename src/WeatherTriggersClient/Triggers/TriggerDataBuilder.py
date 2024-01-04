from abc import ABC, abstractmethod
from src.WeatherTriggersClient.Triggers import TriggerTimePeriod
from src.WeatherTriggersClient.Triggers.TriggerArea import BaseTriggerArea
from src.WeatherTriggersClient.Triggers.TriggerCondition import TriggerConditionCollection
from src.WeatherTriggersClient.Triggers.Exceptions import NotImplemented


class TriggerDataBuilder(ABC):

    @abstractmethod
    def build_time_period(self, time_period: TriggerTimePeriod):
        pass

    @abstractmethod
    def build_conditions(self, conditions: TriggerConditionCollection):
        pass

    @abstractmethod
    def build_area(self, area: BaseTriggerArea):
        pass

    @abstractmethod
    def getAndFinishBuild(self):
        pass


class GenericBuilderWithoutArea(TriggerDataBuilder):

    def __init__(self):
        self._data_build = {}

    def build_time_period(self, time_period: TriggerTimePeriod):
        self._data_build["time_period"] = {
            "start": {
                "expression": time_period.start.expression,
                "amount": time_period.start.amount
            },
            "end": {
                "expression": time_period.end.expression,
                "amount": time_period.end.amount
            }
        }

    def build_conditions(self, conditions: TriggerConditionCollection):
        get_condition_dict = lambda x: {
            "name": x.name,
            "expression": x.expression,
            "amount": x.amount

        }
        self._data_build["condition"] = [get_condition_dict(condition) for condition in conditions.get_collection()]

    def build_area(self, area: BaseTriggerArea):
        raise NotImplemented("Area build is not implemented")

    def getAndFinishBuild(self):
        finished_build = self._data_build.copy()
        self._data_build.clear()
        return finished_build


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
