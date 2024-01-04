from src.WeatherMapsClient.Maps.BaseMap import BaseMap
from src.WeatherMapsClient.Exceptions import raise_out_of_range_exception
from src.WeatherMapsClient.Maps.MapBoundsChecker import MapBoundsChecker


class BaseMapWithBoundsChecking(BaseMap):

    def __init__(self, x, y, z, bounds_checker: MapBoundsChecker):
        super().__init__(x, y, z)
        if bounds_checker is None:
            raise TypeError("Bound checker is not provided - None")
        self._bound_checker = bounds_checker
        if not bounds_checker.is_value_in_bounds(x):
            self._raise_x_or_y_out_of_range()
        if not bounds_checker.is_value_in_bounds(y):
            self._raise_x_or_y_out_of_range()

    def _raise_x_or_y_out_of_range(self):
        raise_out_of_range_exception(
            lower_bound=self._bound_checker.lower_bound,
            upper_bound=self._bound_checker.upper_bound
        )

    @property
    def z(self):
        return self._area

    @z.setter
    def z(self, val):
        self._area = val

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        if not isinstance(value, int):
            value = int(value)
        if self._bound_checker:
            if self._bound_checker.is_value_in_bounds(value):
                self._x = value
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        if not isinstance(value, int):
            value = int(value)
        if self._bound_checker:
            if self._bound_checker.is_value_in_bounds(value):
                self._y = value
        else:
            self._y = value
