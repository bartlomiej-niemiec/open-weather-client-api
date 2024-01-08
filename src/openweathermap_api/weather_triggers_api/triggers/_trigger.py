from dataclasses import dataclass
from typing import List

from src.openweathermap_api.weather_triggers_api.triggers._trigger_condition import TriggerCondition
from src.openweathermap_api.weather_triggers_api.triggers._trigger_time_period import TriggerTimePeriod
from src.openweathermap_api.weather_triggers_api.triggers._trigger_area import BaseTriggerArea


@dataclass
class Trigger:
    time_period: TriggerTimePeriod
    conditions: List[TriggerCondition]
    area: BaseTriggerArea
