from src.WeatherMapsClient.exceptions import raise_out_of_range_exception


class MapXYBounds:

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def is_value_in_bounds(self, value):
        if not (self.lower_bound <= value <= self.upper_bound):
            raise_out_of_range_exception(self.lower_bound, self.upper_bound)
        else:
            return True
