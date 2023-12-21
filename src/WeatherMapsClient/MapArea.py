from src.WeatherMapsClient.constants import MapZoom, ZoomCoordinatesLowerBound, ZoomCoordinatesUpperBound
from src.WeatherMapsClient.MapsCoordinates import MapCoordinates


class BaseMap:

    def __init__(self, area: int, coordinates=None):
        self._area = area
        self.coordinates = coordinates

    @property
    def z(self):
        return self._area

    @z.setter
    def z(self, z):
        self._area = z


class WorldwideSizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.Worldwide,
            coordinates=MapCoordinates(
                lower_bound=ZoomCoordinatesLowerBound.Worldwide,
                upper_bound=ZoomCoordinatesUpperBound.Worldwide
            )
        )


class OneQuarterOfTheWorldSizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.OneQuarterOfTheWorld,
            coordinates=MapCoordinates(
                lower_bound=ZoomCoordinatesLowerBound.OneQuarterOfTheWorld,
                upper_bound=ZoomCoordinatesUpperBound.OneQuarterOfTheWorld
            )
        )


class SubcontinentalSizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.Subcontinental,
            coordinates=MapCoordinates(
                lower_bound=ZoomCoordinatesLowerBound.Subcontinental,
                upper_bound=ZoomCoordinatesUpperBound.Subcontinental
            )
        )


class LargestCountryeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.LargestCountry,
            coordinates=MapCoordinates(
                lower_bound=ZoomCoordinatesLowerBound.LargestCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargestCountry
            )
        )


class LargestAsiaCountrySizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.LargestAsiaCountry,
            coordinates=MapCoordinates(
                lower_bound=ZoomCoordinatesLowerBound.LargestAsiaCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargestAsiaCountry
            )
        )


class LargeAfricanCountrySizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.LargeAfricanCountry,
            coordinates=MapCoordinates(
                lower_bound=ZoomCoordinatesLowerBound.LargeAfricanCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargeAfricanCountry
            )
        )


class LargeEuropeanCountrySizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.LargeEuropeanCountry,
            coordinates=MapCoordinates(
                lower_bound=ZoomCoordinatesLowerBound.LargeEuropeanCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargeEuropeanCountry
            )
        )


class SmallCountrySizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.SmallCountry,
            coordinates=MapCoordinates(
                lower_bound=ZoomCoordinatesLowerBound.SmallCountry,
                upper_bound=ZoomCoordinatesUpperBound.SmallCountry
            )
        )


class LargeMetropolitanSizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.LargeMetropolitan,
            coordinates=MapCoordinates(
                lower_bound=ZoomCoordinatesLowerBound.LargeMetropolitan,
                upper_bound=ZoomCoordinatesUpperBound.LargeMetropolitan
            )
        )


class MetropolitanSizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.Metropolitan,
            coordinates=MapCoordinates(
                lower_bound=ZoomCoordinatesLowerBound.Metropolitan,
                upper_bound=ZoomCoordinatesUpperBound.Metropolitan
            )
        )