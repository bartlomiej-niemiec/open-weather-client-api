from dataclasses import dataclass
from typing import List

from openweather_api.WeatherTriggersClient.Triggers.TriggerCondition import TriggerCondition
from openweather_api.WeatherTriggersClient.Triggers.TriggerTimePeriod import TriggerTimePeriod
from openweather_api.WeatherTriggersClient.Triggers.TriggerArea import BaseTriggerArea


@dataclass
class Trigger:
    time_period: TriggerTimePeriod
    conditions: List[TriggerCondition]
    area: BaseTriggerArea
