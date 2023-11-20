from constants import MapArea, CoordinatesLowerBound, CoordinatesUpperBound
from src.WeatherMapsClient.exceptions import raise_out_of_range_exception, UnsupportedZoomLevel
from collections import namedtuple

MapParameters = namedtuple('MapParameters', ['map_area', 'map_coordinates'])


class MapParametersCreator:
    LOWER_ZOOM_LEVEL = 0
    GREATEST_ZOOM_LEVEL = 9

    @staticmethod
    def create(map_area: int):
        if map_area == MapArea.Worldwide:
            map_coordinates = MapCoordinates(
                CoordinatesLowerBound.zero,
                CoordinatesUpperBound.zero,
            )
            map_parameters = MapParameters(map_area, map_coordinates)

            return map_parameters

        elif map_area == MapArea.OneQuarterOfTheWorld:
            map_coordinates = MapCoordinates(
                CoordinatesLowerBound.one,
                CoordinatesUpperBound.one,
            )
            map_parameters = MapParameters(map_area, map_coordinates)

            return map_parameters

        elif map_area == MapArea.Subcontinental:
            map_coordinates = MapCoordinates(
                CoordinatesLowerBound.two,
                CoordinatesUpperBound.two,
            )

            map_parameters = MapParameters(map_area, map_coordinates)

            return map_parameters

        elif map_area == MapArea.LargestCountry:
            map_coordinates = MapCoordinates(
                CoordinatesLowerBound.three,
                CoordinatesUpperBound.three,
            )

            map_parameters = MapParameters(map_area, map_coordinates)

            return map_parameters

        elif map_area == MapArea.LargestAsiaCountry:
            map_coordinates = MapCoordinates(
                CoordinatesLowerBound.four,
                CoordinatesUpperBound.four,
            )

            map_parameters = MapParameters(map_area, map_coordinates)

            return map_parameters

        elif map_area == MapArea.LargeAfricanCountry:
            map_coordinates = MapCoordinates(
                CoordinatesLowerBound.five,
                CoordinatesUpperBound.five,
            )

            map_parameters = MapParameters(map_area, map_coordinates)

            return map_parameters

        elif map_area == MapArea.LargeEuropeanCountry:
            map_coordinates = MapCoordinates(
                CoordinatesLowerBound.six,
                CoordinatesUpperBound.six,
            )

            map_parameters = MapParameters(map_area, map_coordinates)

            return map_parameters

        elif map_area == MapArea.SmallCountry:
            map_coordinates = MapCoordinates(
                CoordinatesLowerBound.seven,
                CoordinatesUpperBound.seven,
            )

            map_parameters = MapParameters(map_area, map_coordinates)

            return map_parameters

        elif map_area == MapArea.LargeMetropolitan:
            map_coordinates = MapCoordinates(
                CoordinatesLowerBound.eight,
                CoordinatesUpperBound.eight,
            )

            map_parameters = MapParameters(map_area, map_coordinates)

            return map_parameters

        elif map_area == MapArea.Metropolitan:
            map_coordinates = MapCoordinates(
                CoordinatesLowerBound.nine,
                CoordinatesUpperBound.nine,
            )

            map_parameters = MapParameters(map_area, map_coordinates)

            return map_parameters
        else:
            raise UnsupportedZoomLevel(f"Given zoom level is not possible.",
                                       f"Zoom level should be in range {MapParametersCreator.LOWER_ZOOM_LEVEL}"
                                       f"to {MapParametersCreator.GREATEST_ZOOM_LEVEL}")


class MapCoordinates:

    def __init__(self, lower_bound, upper_bound):
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound
        self._x = self._y = (lower_bound + upper_bound) // 2

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        if self._check_value(value):
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        if self._check_value(value):
            self._y = value

    def _check_value(self, value):
        return self._is_value_type_correct(value) and self._is_value_in_bounds(value)

    def _is_value_type_correct(self, value):
        if not isinstance(value, int):
            raise TypeError("Only integers are possible")
        return True

    def _is_value_in_bounds(self, value):
        if not (self._lower_bound <= value <= self._upper_bound):
            raise_out_of_range_exception(self._lower_bound, self._upper_bound)
        else:
            return True
