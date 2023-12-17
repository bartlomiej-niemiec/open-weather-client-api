from src.WeatherTriggersClient.Triggers.TriggerArea import PointTriggerArea
from src.WeatherTriggersClient.Triggers.TriggerDataBuilder import PointTriggerBuilder
from src.WeatherTriggersClient.Triggers.Trigger import Trigger
from src.WeatherTriggersClient.Triggers.TriggerDataBuilder import TriggerDataBuilder


class TriggerDataFactory:

    @staticmethod
    def create_trigger_data(trigger: Trigger):
        builder = None
        if isinstance(trigger.area, PointTriggerArea):
            builder = PointTriggerBuilder()

        build_trigger_data(builder, trigger)
        return builder.getAndFinishBuild()


def build_trigger_data(builder: TriggerDataBuilder, trigger: Trigger):
    builder.build_conditions(trigger.conditions)
    builder.build_time_period(trigger.time_period)
    builder.build_area(trigger.area)
