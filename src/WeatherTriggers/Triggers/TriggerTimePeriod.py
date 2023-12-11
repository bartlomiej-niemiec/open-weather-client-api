from dataclasses import dataclass
from src.WeatherTriggers.Triggers.IToDict import IToDict


@dataclass
class TimePeriod(IToDict):
    expression: str  # Specifies how to process value of the amount field
    amount: int  # number of milliseconds

    def toDict(self) -> dict:
        return self.__dict__


@dataclass
class TriggerTimePeriod(IToDict):
    start: TimePeriod  # beginning of time interval used to check conditions
    end: TimePeriod  # end of time interval used to check conditions

    def toDict(self) -> dict:
        trigger_time_period_dict = {
            "start": self.start.toDict(),
            "end": self.end.toDict()
        }
        return trigger_time_period_dict
