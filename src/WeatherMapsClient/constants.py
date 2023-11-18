from enum import IntEnum


class CoordinatesLowerBound:
    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0


class CoordinatesUpperBound:
    zero = 1
    one = 1
    two = 3
    three = 7
    four = 15
    five = 31
    six = 63
    seven = 127
    eight = 255
    nine = 511


class Zoom(IntEnum):
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
