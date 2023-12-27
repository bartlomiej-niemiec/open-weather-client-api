from src.GenericClient.base_client import Client, parse_response
from src.WeatherTriggersClient.Triggers.Trigger import Trigger
from src.WeatherTriggersClient.Triggers.TriggerDataFactory import TriggerDataFactory


class WeatherTriggersClient(Client):
    _API_URL = "http://api.openweathermap.org/data/3.0/triggers"

    def register_trigger(self, trigger_parameters: Trigger):
        post_request_response = self._request(
            'POST',
            url=self._API_URL,
            data=TriggerDataFactory.create_trigger_data(trigger_parameters)
        )
        response = parse_response(post_request_response)
        return response

    def get_alerts_by_trigger(self, trigger_id: str):
        get_request_response = self._request(
            'GET',
            url=self._get_api_url_with_extra_arguments(trigger_id),
            data={}

        )
        response = parse_response(get_request_response)
        return response

    def get_all_trigers(self):
        get_request_response = self._request(
            'GET',
            url=self._API_URL,
            data={}

        )
        response = parse_response(get_request_response)
        return response

    def update_trigger(self, trigger_parameters: Trigger, trigger_id: str):
        post_request_response = self._request(
            'PUT',
            url=self._get_api_url_with_extra_arguments(trigger_id),
            data=TriggerDataFactory.create_trigger_data(trigger_parameters)
        )
        response = parse_response(post_request_response)
        return response

    def delete_trigger(self, trigger_id: str):
        delete_request_response = self._request(
            'DELETE',
            url=self._get_api_url_with_extra_arguments(trigger_id),
            data={}
        )
        response = parse_response(delete_request_response)
        return response

    def get_history_alerts(self, trigger_id: str, alert_id: str):
        get_request_response = self._request(
            'GET',
            url=self._get_api_url_with_extra_arguments(trigger_id, "history", alert_id),
            data={}
        )
        response = parse_response(get_request_response)
        return response

    def get_all_history_alerts(self, trigger_id: str):
        get_request_response = self._request(
            'GET',
            url=self._get_api_url_with_extra_arguments(trigger_id, "history"),
            data={}
        )
        response = parse_response(get_request_response)
        return response

    def delete_history_alert(self, trigger_id: str, alert_id: str):
        delete_request_response = self._request(
            'GET',
            url=self._get_api_url_with_extra_arguments(trigger_id, "history", alert_id),
            data={}
        )
        response = parse_response(delete_request_response)
        return response

    def delete_all_history_alert(self, trigger_id: str):
        delete_request_response = self._request(
            'GET',
            url=self._get_api_url_with_extra_arguments(trigger_id, "history"),
            data={}
        )
        response = parse_response(delete_request_response)
        return response

    def _get_api_url_with_extra_arguments(self, *args):
        api_url_with_args = self._API_URL
        for arg in args:
            api_url_with_args += f"/{arg}"
        return api_url_with_args
