from src.WeatherMapsClient.exceptions import raise_out_of_range_exception


class MapCoordinates:

    def __init__(self, lower_bound, upper_bound):
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound
        # set default coordinates to the middle value of bounds
        self._x = self._y = (lower_bound + upper_bound) // 2

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        if not isinstance(value, int):
            value = int(value)
        if self._is_value_in_bounds(value):
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        if not isinstance(value, int):
            value = int(value)
        if self._is_value_in_bounds(value):
            self._y = value

    def _is_value_in_bounds(self, value):
        if not (self._lower_bound <= value <= self._upper_bound):
            raise_out_of_range_exception(self._lower_bound, self._upper_bound)
        else:
            return True
