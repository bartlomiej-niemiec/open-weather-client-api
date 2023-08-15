class ZoomLevel:
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9


def get_x_y_range(zoom_lvl: ZoomLevel):
    if zoom_lvl == 0:
        lower_bound, upper_bound = 1, 1
    elif zoom_lvl == 1:
        lower_bound, upper_bound = 0, 1
    elif zoom_lvl == 2:
        lower_bound, upper_bound = 0, 3
    elif zoom_lvl == 3:
        lower_bound, upper_bound = 0, 7
    elif zoom_lvl == 4:
        lower_bound, upper_bound = 0, 15
    elif zoom_lvl == 5:
        lower_bound, upper_bound = 0, 31
    elif zoom_lvl == 6:
        lower_bound, upper_bound = 0, 63
    elif zoom_lvl == 7:
        lower_bound, upper_bound = 0, 127
    elif zoom_lvl == 8:
        lower_bound, upper_bound = 0, 255
    elif zoom_lvl == 9:
        lower_bound, upper_bound = 0, 511
    else:
        raise "Given zoom level is not supported"
    return lower_bound, upper_bound


class MapCoordinates:

    def __init__(self, zoom_level: ZoomLevel):
        self.z = zoom_level
        lower_bound, upper_bound = get_x_y_range(self.z)
        self.x = self.y = (lower_bound + upper_bound) // 2

    def _check_value_correctness(self, value):
        value_correct = False
        lower_bound, upper_bound = get_x_y_range(self.z)
        if lower_bound <= value <= upper_bound:
            value_correct = True
        return value_correct

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value: int):
        if value != type(int):
            raise "X and Y "
        if self._check_value_correctness(value):
            self.x = value
        else:
            raise "Value not in allowed range"

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value: int):
        if value != type(int):
            raise "X and Y "
        if self._check_value_correctness(value):
            self.y = value
        else:
            raise "Value not in allowed range"

    @property
    def z(self):
        return self.z

    @z.setter
    def z(self, zoom_level: ZoomLevel):
        lower_bound, upper_bound = get_x_y_range(zoom_level)
        self.z = zoom_level
        self.x = self.y = (lower_bound + upper_bound) // 2
