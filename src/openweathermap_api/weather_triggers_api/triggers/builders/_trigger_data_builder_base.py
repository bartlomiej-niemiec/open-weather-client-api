from abc import ABC, abstractmethod
from typing import List

from src.openweathermap_api.weather_triggers_api.triggers import TriggerTimePeriod
from src.openweathermap_api.weather_triggers_api.triggers._trigger_area import BaseTriggerArea
from src.openweathermap_api.weather_triggers_api.triggers._trigger_condition import TriggerCondition


class TriggerDataBuilder(ABC):

    @abstractmethod
    def build_time_period(self, time_period: TriggerTimePeriod):
        pass

    @abstractmethod
    def build_conditions(self, conditions: List[TriggerCondition]):
        pass

    @abstractmethod
    def build_area(self, area: BaseTriggerArea):
        pass

    @abstractmethod
    def getAndFinishBuild(self):
        pass
