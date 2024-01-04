class BaseMap:

    def __init__(self, x: int, y: int, z: int):
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
