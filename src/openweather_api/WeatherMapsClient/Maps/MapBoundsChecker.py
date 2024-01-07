class MapBoundsChecker:
    """XY coordinates checker."""
    def __init__(self, lower_bound, upper_bound):
        """Initialize object.

        :param lower_bound: lower bound of XY coordinates.
        :param upper_bound: upper bound of XY coordinates.
        """
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def is_value_in_bounds(self, value):
        """check if value is in bounds range.

        :param value: x/y coordinate value.
        :return: true if is in bounds.
        """
        return self.lower_bound <= value <= self.upper_bound

