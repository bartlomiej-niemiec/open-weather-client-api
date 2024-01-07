from dataclasses import dataclass


@dataclass
class TimePeriod:
    expression: str  # Specifies how to process value of the amount field
    amount: int  # number of milliseconds


@dataclass
class TriggerTimePeriod:
    start: TimePeriod  # beginning of time interval used to check conditions
    end: TimePeriod  # end of time interval used to check conditions
