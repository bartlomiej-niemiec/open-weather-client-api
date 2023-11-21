def raise_out_of_range_exception(lower_bound, upper_bound):
    raise ValueOutOfRange('Coordinate should be in range', lower_bound, 'to', upper_bound)


class ValueOutOfRange(Exception):
    pass


class UnsupportedZoomLevel(Exception):
    pass


class ImageFormatNotAllowed(Exception):
    pass
