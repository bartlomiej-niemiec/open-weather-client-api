from constants import Zoom, CoordinatesLowerBound, CoordinatesUpperBound


class MapCoordinatesCreator:

    LOWER_ZOOM_LEVEL = 0
    GREATEST_ZOOM_LEVEL = 0

    @staticmethod
    def create(zoom_level: int):
        if Zoom.zero:
            return MapCoordinates(
                CoordinatesLowerBound.zero,
                CoordinatesUpperBound.zero,
                zoom_level
            )
        elif Zoom.one:
            return MapCoordinates(
                CoordinatesLowerBound.one,
                CoordinatesUpperBound.one,
                zoom_level
            )
        elif Zoom.two:
            return MapCoordinates(
                CoordinatesLowerBound.two,
                CoordinatesUpperBound.two,
                zoom_level
            )
        elif Zoom.three:
            return MapCoordinates(
                CoordinatesLowerBound.three,
                CoordinatesUpperBound.three,
                zoom_level
            )
        elif Zoom.four:
            return MapCoordinates(
                CoordinatesLowerBound.four,
                CoordinatesUpperBound.four,
                zoom_level
            )
        elif Zoom.five:
            return MapCoordinates(
                CoordinatesLowerBound.five,
                CoordinatesUpperBound.five,
                zoom_level
            )
        elif Zoom.six:
            return MapCoordinates(
                CoordinatesLowerBound.six,
                CoordinatesUpperBound.six,
                zoom_level
            )
        elif Zoom.seven:
            return MapCoordinates(
                CoordinatesLowerBound.seven,
                CoordinatesUpperBound.seven,
                zoom_level
            )
        elif Zoom.eight:
            return MapCoordinates(
                CoordinatesLowerBound.eight,
                CoordinatesUpperBound.eight,
                zoom_level
            )
        elif Zoom.nine:
            return MapCoordinates(
                CoordinatesLowerBound.nine,
                CoordinatesUpperBound.nine,
                zoom_level
            )
        else:
            raise UnsupportedZoomLevel(f"Given zoom level is not possible.",
                                       f"Zoom level should be in range {MapCoordinatesCreator.LOWER_ZOOM_LEVEL}"
                                       f"to {MapCoordinatesCreator.GREATEST_ZOOM_LEVEL}")


class UnsupportedZoomLevel(Exception):
    pass


class MapCoordinates:

    def __init__(self, lower_bound, upper_bound, z):
        self._z = z
        self.x = self.y = (lower_bound + upper_bound) // 2
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value: int):
        if self._is_coordinate_type_correct(value) and self._check_value_in_bounds(value):
            self.x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value: int):
        if self._is_coordinate_type_correct(value) and self._check_value_in_bounds(value):
            self.y = value

    @property
    def z(self):
        return self._z

    def _is_coordinate_type_correct(self, value):
        if isinstance(value, int):
            raise TypeError("Only integers are possible")
        return True

    def _check_value_in_bounds(self, value):
        if not (self._lower_bound <= value <= self._upper_bound):
            raise_out_of_range_exception(self._lower_bound, self._upper_bound)
        else:
            return True


def raise_out_of_range_exception(lower_bound, upper_bound):
    raise ValueOutOfRange('Coordinate should be in range', lower_bound, 'to', upper_bound)


class ValueOutOfRange(Exception):
    pass
