from abc import ABC, abstractmethod
from typing import List

from src.openweathermap_api.WeatherTriggersClientAPI.Triggers import TriggerTimePeriod
from src.openweathermap_api.WeatherTriggersClientAPI.Triggers._TriggerArea import BaseTriggerArea
from src.openweathermap_api.WeatherTriggersClientAPI.Triggers._TriggerCondition import TriggerCondition


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
