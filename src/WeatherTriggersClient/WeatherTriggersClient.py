from src.GenericClient.base_client import Client, parse_response
from src.WeatherTriggersClient.Triggers.Trigger import Trigger
from src.WeatherTriggersClient.Triggers.TriggerArea import PointTriggerArea, CoordinatesPoint
from src.WeatherTriggersClient.Triggers.TriggerCondition import TriggerConditionCollection, SingleTriggerCondition
from src.WeatherTriggersClient.Triggers.TriggerDataFactory import TriggerDataFactory
from src.WeatherTriggersClient.Triggers.TriggerTimePeriod import TriggerTimePeriod, TimePeriod


class WeatherTriggersClient(Client):
    _API_URL = "http://api.openweathermap.org/data/3.0/triggers"

    def register_station(self, register_trigger: Trigger):
        post_request_response = self._post_request(
            url=self._API_URL,
            data=TriggerDataFactory.create_trigger_data(register_trigger)
        )
        response = parse_response(post_request_response)
        return response


def create_trigger():
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

    return trigger


if __name__ == "__main__":
    API_KEY = ""
    trigger_client = WeatherTriggersClient(API_KEY)
    response = trigger_client.register_station(create_trigger())
    print(response)
