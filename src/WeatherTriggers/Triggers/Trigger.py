from dataclasses import dataclass
from src.WeatherTriggers.Triggers.IToDict import IToDict
from src.WeatherTriggers.Triggers.TriggerCondition import TriggerConditionCollection, SingleTriggerCondition
from src.WeatherTriggers.Triggers.TriggerTimePeriod import TriggerTimePeriod, TimePeriod
from src.WeatherTriggers.Triggers.TriggerArea import BaseTriggerArea, PointTriggerArea, CoordinatesPoint


@dataclass
class Trigger(IToDict):
    time_period: TriggerTimePeriod
    conditions: TriggerConditionCollection
    area: BaseTriggerArea

    def toDict(self) -> dict:
        trigger_dict = {}
        for attribute in self.__dir__():
            attribute_handle = self.__getattribute__(attribute)
            if isinstance(attribute_handle, IToDict):
                trigger_dict[attribute] = attribute_handle.toDict()
        return trigger_dict


if __name__ == "__main__":
    time_period = TriggerTimePeriod(
        start=TimePeriod(
            expression="after",
            amount=132000000

        ),
        end=TimePeriod(
            expression="after",
            amount=432000000
        )
    )

    trigger_condition = TriggerConditionCollection()
    trigger_condition.add_condition(
        SingleTriggerCondition(
            amount=299,
            expression="$gt",
            name="temp"
        )
    )
    trigger_area = PointTriggerArea(
        CoordinatesPoint(53, 57),
    )

    trigger = Trigger(
        time_period=time_period,
        conditions=trigger_condition,
        area=trigger_area
    )

    print(trigger.toDict())
