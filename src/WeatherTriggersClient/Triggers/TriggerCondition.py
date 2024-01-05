from dataclasses import dataclass


@dataclass
class TriggerCondition:
    name: str  # The name of the parameter to be compared with.
    expression: str  # The expression which will be used to compare.
    amount: int  # Numerical value to be compared with
