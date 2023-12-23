from src.WeatherMapsClient.MapCoordinateBounds import MapXYBounds


class BaseMap:

    def __init__(self, area: int, bounds: MapXYBounds = None):
        self._area = area
        self._bounds = bounds
        # set default value to middle point
        self._x = self._y = (bounds.lower_bound + bounds.upper_bound) // 2

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
        if self._bounds:
            if self._bounds.is_value_in_bounds(value):
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
        if self._bounds:
            if self._bounds.is_value_in_bounds(value):
                self._y = value
        else:
            self._y = value
