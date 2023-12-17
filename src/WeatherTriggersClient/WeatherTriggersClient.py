from src.GenericClient.base_client import Client, parse_response
from src.WeatherTriggersClient.Triggers.Trigger import Trigger
from src.WeatherTriggersClient.Triggers.TriggerArea import PointTriggerArea, CoordinatesPoint
from src.WeatherTriggersClient.Triggers.TriggerCondition import TriggerConditionCollection, SingleTriggerCondition
from src.WeatherTriggersClient.Triggers.TriggerDataFactory import TriggerDataFactory
from src.WeatherTriggersClient.Triggers.TriggerTimePeriod import TriggerTimePeriod, TimePeriod


class WeatherTriggersClient(Client):
    _API_URL = "http://api.openweathermap.org/data/3.0/triggers"

    def register_station(self, trigger_parameters: Trigger):
        post_request_response = self._post_request(
            url=self._API_URL,
            data=TriggerDataFactory.create_trigger_data(trigger_parameters)
        )
        response = parse_response(post_request_response)
        return response

    def get_alerts_by_trigger(self, trigger_id: str):
        get_request_response = self._get_request(
            url=self._get_api_url_with_extra_arguments(trigger_id),
            params={}

        )
        response = parse_response(get_request_response)
        return response

    def get_all_trigers(self):
        get_request_response = self._get_request(
            url=self._API_URL,
            params={}

        )
        response = parse_response(get_request_response)
        return response

    def update_trigger(self, trigger_parameters: Trigger, trigger_id: str):
        post_request_response = self._put_request(
            url=self._get_api_url_with_extra_arguments(trigger_id),
            data=TriggerDataFactory.create_trigger_data(trigger_parameters)
        )
        response = parse_response(post_request_response)
        return response

    def delete_trigger(self, trigger_id: str):
        delete_request_response = self._delete_request(
            url=self._get_api_url_with_extra_arguments(trigger_id),
            params={}
        )
        response = parse_response(delete_request_response)
        return response

    def get_history_alerts(self, trigger_id: str, alert_id: str):
        get_request_response = self._get_request(
            url=self._get_api_url_with_extra_arguments(trigger_id, "history", alert_id),
            params={}
        )
        response = parse_response(get_request_response)
        return response

    def get_all_history_alerts(self, trigger_id: str):
        get_request_response = self._get_request(
            url=self._get_api_url_with_extra_arguments(trigger_id, "history"),
            params={}
        )
        response = parse_response(get_request_response)
        return response

    def delete_history_alert(self, trigger_id: str, alert_id: str):
        delete_request_response = self._delete_request(
            url=self._get_api_url_with_extra_arguments(trigger_id, "history", alert_id),
            params={}
        )
        response = parse_response(delete_request_response)
        return response

    def delete_all_history_alert(self, trigger_id: str):
        delete_request_response = self._delete_request(
            url=self._get_api_url_with_extra_arguments(trigger_id, "history"),
            params={}
        )
        response = parse_response(delete_request_response)
        return response

    def _get_api_url_with_extra_arguments(self, *args):
        api_url_with_args = self._API_URL
        for arg in args:
            api_url_with_args += f"/{arg}"
        return api_url_with_args


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
    register_triggers = trigger_client.get_all_trigers()



