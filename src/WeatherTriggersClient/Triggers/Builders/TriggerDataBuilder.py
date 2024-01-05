from abc import ABC, abstractmethod
from typing import List

from src.WeatherTriggersClient.Triggers import TriggerTimePeriod
from src.WeatherTriggersClient.Triggers.TriggerArea import BaseTriggerArea
from src.WeatherTriggersClient.Triggers.TriggerCondition import TriggerCondition


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
