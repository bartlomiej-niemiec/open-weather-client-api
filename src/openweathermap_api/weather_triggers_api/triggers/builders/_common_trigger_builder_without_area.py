from typing import List
from src.openweathermap_api.weather_triggers_api.triggers import TriggerTimePeriod
from src.openweathermap_api.weather_triggers_api.triggers._trigger_exceptions import NotImplemented
from src.openweathermap_api.weather_triggers_api.triggers._trigger_area import BaseTriggerArea
from src.openweathermap_api.weather_triggers_api.triggers._trigger_condition import TriggerCondition
from src.openweathermap_api.weather_triggers_api.triggers.builders._trigger_data_builder_base import TriggerDataBuilder


class CommonBuilderWithoutArea(TriggerDataBuilder):

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

    def build_conditions(self, conditions: List[TriggerCondition]):
        get_condition_dict = lambda x: {
            "name": x.name,
            "expression": x.expression,
            "amount": x.amount

        }
        if isinstance(conditions, list):
            self._data_build["condition"] = []
            for condition in conditions:
                if isinstance(condition, TriggerCondition):
                    self._data_build["condition"].append(get_condition_dict(condition))
                else:
                    raise TypeError("Trigger conditions list should include only 'TriggerCondition' objects.")
        else:
            if isinstance(conditions, TriggerCondition):
                self._data_build["condition"] = [get_condition_dict(conditions)]

    def build_area(self, area: BaseTriggerArea):
        raise NotImplemented("Area build is not implemented")

    def getAndFinishBuild(self):
        finished_build = self._data_build.copy()
        self._data_build.clear()
        return finished_build
