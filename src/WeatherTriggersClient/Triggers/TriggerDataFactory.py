from src.WeatherTriggersClient.Triggers.TriggerArea import PointTriggerArea, MultiPointTriggerArea,\
    PolygonTriggerArea, MultiPolygonTriggerArea
from src.WeatherTriggersClient.Triggers.Builders.TriggerBuildersWithArea import PointTriggerBuilder, MultiPointTriggerBuilder, \
    PolygonTriggerBuilder, MultiPolygonTriggerBuilder
from src.WeatherTriggersClient.Triggers.Trigger import Trigger
from src.WeatherTriggersClient.Triggers.Builders.TriggerDataBuilder import TriggerDataBuilder


class TriggerDataFactory:

    @staticmethod
    def create_trigger_data(trigger: Trigger):
        builder = None
        if isinstance(trigger.area, PointTriggerArea):
            builder = PointTriggerBuilder()
        elif isinstance(trigger.area, MultiPointTriggerArea):
            builder = MultiPointTriggerBuilder()
        elif isinstance(trigger.area, PolygonTriggerArea):
            builder = PolygonTriggerBuilder()
        elif isinstance(trigger.area, MultiPolygonTriggerArea):
            builder = MultiPolygonTriggerBuilder()
        else:
            raise Exception("Unexpected trigger")
        build_trigger_data(builder, trigger)
        return builder.getAndFinishBuild()


def build_trigger_data(builder: TriggerDataBuilder, trigger: Trigger):
    builder.build_conditions(trigger.conditions)
    builder.build_time_period(trigger.time_period)
    builder.build_area(trigger.area)
