from dataclasses import dataclass
from src.WeatherTriggers.Triggers.IToDict import IToDict


@dataclass
class SingleTriggerCondition(IToDict):
    name: str  # The name of the parameter to be compared with.
    expression: str  # The expression which will be used to compare.
    amount: int  # Numerical value to be compared with

    def toDict(self) -> dict:
        return self.__dict__


class TriggerConditionCollection(IToDict):

    def __init__(self):
        self._trigger_condition_list = []

    def add_condition(self, condition: SingleTriggerCondition):
        self._trigger_condition_list.append(condition)

    def get_collection(self):
        return self._trigger_condition_list

    def remove_condition_at_index(self, index):
        self._trigger_condition_list.pop(index)

    def toDict(self) -> dict:
        temp_trigger_condition_list = self._trigger_condition_list.copy()
        for i in range(len(temp_trigger_condition_list)):
            temp_trigger_condition_list[i] = temp_trigger_condition_list[i].toDict()
        return temp_trigger_condition_list
