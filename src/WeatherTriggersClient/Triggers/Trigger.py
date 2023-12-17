from dataclasses import dataclass
from src.WeatherTriggersClient.Triggers.TriggerCondition import TriggerConditionCollection
from src.WeatherTriggersClient.Triggers.TriggerTimePeriod import TriggerTimePeriod
from src.WeatherTriggersClient.Triggers.TriggerArea import BaseTriggerArea


@dataclass
class Trigger:
    time_period: TriggerTimePeriod
    conditions: TriggerConditionCollection
    area: BaseTriggerArea
