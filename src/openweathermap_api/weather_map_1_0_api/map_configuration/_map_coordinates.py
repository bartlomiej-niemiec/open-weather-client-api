class MapCoordinates:
    """Data structure holding map coordinates (x,y) and zoom level (z)"""
    def __init__(self, x: int, y: int, z: int):
        """Initialize object.

        :param x: value of x coordinate.
        :param y: value of y coordinate.
        :param z: value of z/zoom coordinate.
        """
        self._area = z
        self._x = x
        self._y = y

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
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value
