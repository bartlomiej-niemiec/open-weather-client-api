def _check_type(parameter, desired_type):
    type_ok = True
    if not isinstance(parameter, desired_type):
        type_ok = False
    return type_ok


def _raise_type_exception(parameter, desired_type):
    raise TypeError(f'Type {type(parameter)} not allowed, it should be {desired_type}')


def _check_range(start, end, number):
    range_ok = True
    if not start <= number <= end:
        range_ok = False
    return range_ok


def _raise_range_exception(start, end):
    raise ValueError(f'Value should be in range: <{start}; {end}>')
