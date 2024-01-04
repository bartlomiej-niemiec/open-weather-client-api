class MapBoundsChecker:

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def is_value_in_bounds(self, value):
        return self.lower_bound <= value <= self.upper_bound
