from dataclasses import dataclass
from datetime import datetime
import time


@dataclass
class UTCtoUnixTime:
    """Display date as a unix time format."""
    year: int
    month: int
    day: int
    hour: int = 0
    minutes: int = 0

    def _to_unix_timestamp(self):
        date_time = datetime(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minutes
        )
        return time.mktime(date_time.timetuple())

    def __str__(self):
        return str(self.__int__())

    def __int__(self):
        return int(self._to_unix_timestamp())

    def __repr__(self):
        return self.__str__()
