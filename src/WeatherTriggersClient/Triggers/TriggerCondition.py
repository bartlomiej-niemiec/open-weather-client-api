from dataclasses import dataclass


@dataclass
class SingleTriggerCondition:
    name: str  # The name of the parameter to be compared with.
    expression: str  # The expression which will be used to compare.
    amount: int  # Numerical value to be compared with


class TriggerConditionCollection:

    def __init__(self):
        self._trigger_condition_list = []

    def add_condition(self, condition: SingleTriggerCondition):
        self._trigger_condition_list.append(condition)

    def get_collection(self):
        return self._trigger_condition_list

    def remove_condition_at_index(self, index):
        self._trigger_condition_list.pop(index)
