class Layers:
    _clouds = "clouds_new"
    _precipitation = "precipitation_new"
    _sea_level_pressure = "pressure_new"
    _wind_speed = "wind_new"
    _temperature = "temp_new"

    _list_layers = [
        _clouds,
        _precipitation,
        _sea_level_pressure,
        _wind_speed,
        _temperature,
    ]

    def __init__(self):
        self._iter_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter_index < len(self._list_layers):
            layer = self._list_layers[self._iter_index]
            self._iter_index += 1
            return layer
        else:
            raise StopIteration

    @property
    def clouds(self):
        return self._clouds

    @property
    def precipitation(self):
        return self._precipitation

    @property
    def sea_level_pressure(self):
        return self._sea_level_pressure

    @property
    def wind_speed(self):
        return self._wind_speed

    @property
    def temperature(self):
        return self._temperature
