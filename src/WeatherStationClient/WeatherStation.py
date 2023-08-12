class Station(dict):

    _allowed_keys = ['external_id', 'name', 'latitude', 'longitude', 'altitude']

    def __init__(self, external_id, name, latitude, longitude, altitude):
        super().__init__({
            'external_id': external_id,
            'name': name,
            'latitude': latitude,
            'longitude': longitude,
            'altitude': altitude
        })

    def __setitem__(self, key, value):
        if key not in self._allowed_keys:
            return
        super().__setitem__(self, key, value)
