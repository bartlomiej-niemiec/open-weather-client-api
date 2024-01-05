from dataclasses import dataclass
from typing import List

from src.WeatherTriggersClient.Triggers.TriggerCondition import TriggerCondition
from src.WeatherTriggersClient.Triggers.TriggerTimePeriod import TriggerTimePeriod
from src.WeatherTriggersClient.Triggers.TriggerArea import BaseTriggerArea


@dataclass
class Trigger:
    time_period: TriggerTimePeriod
    conditions: List[TriggerCondition]
    area: BaseTriggerArea
