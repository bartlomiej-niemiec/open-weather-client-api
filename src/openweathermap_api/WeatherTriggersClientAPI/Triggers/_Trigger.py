from dataclasses import dataclass
from typing import List

from src.openweathermap_api.WeatherTriggersClientAPI.Triggers._TriggerCondition import TriggerCondition
from src.openweathermap_api.WeatherTriggersClientAPI.Triggers._TriggerTimePeriod import TriggerTimePeriod
from src.openweathermap_api.WeatherTriggersClientAPI.Triggers._TriggerArea import BaseTriggerArea


@dataclass
class Trigger:
    time_period: TriggerTimePeriod
    conditions: List[TriggerCondition]
    area: BaseTriggerArea
