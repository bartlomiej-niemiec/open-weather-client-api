from src.WeatherMapsClient.BaseMap import BaseMap
from src.WeatherMapsClient.constants import MapZoom, ZoomCoordinatesLowerBound, ZoomCoordinatesUpperBound
from src.WeatherMapsClient.MapCoordinateBounds import MapXYBounds


class WorldwideSizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.Worldwide,
            bounds=MapXYBounds(
                lower_bound=ZoomCoordinatesLowerBound.Worldwide,
                upper_bound=ZoomCoordinatesUpperBound.Worldwide
            )
        )


class OneQuarterOfTheWorldSizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.OneQuarterOfTheWorld,
            bounds=MapXYBounds(
                lower_bound=ZoomCoordinatesLowerBound.OneQuarterOfTheWorld,
                upper_bound=ZoomCoordinatesUpperBound.OneQuarterOfTheWorld
            )
        )


class SubcontinentalSizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.Subcontinental,
            bounds=MapXYBounds(
                lower_bound=ZoomCoordinatesLowerBound.Subcontinental,
                upper_bound=ZoomCoordinatesUpperBound.Subcontinental
            )
        )


class LargestCountryeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.LargestCountry,
            bounds=MapXYBounds(
                lower_bound=ZoomCoordinatesLowerBound.LargestCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargestCountry
            )
        )


class LargestAsiaCountrySizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.LargestAsiaCountry,
            bounds=MapXYBounds(
                lower_bound=ZoomCoordinatesLowerBound.LargestAsiaCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargestAsiaCountry
            )
        )


class LargeAfricanCountrySizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.LargeAfricanCountry,
            bounds=MapXYBounds(
                lower_bound=ZoomCoordinatesLowerBound.LargeAfricanCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargeAfricanCountry
            )
        )


class LargeEuropeanCountrySizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.LargeEuropeanCountry,
            bounds=MapXYBounds(
                lower_bound=ZoomCoordinatesLowerBound.LargeEuropeanCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargeEuropeanCountry
            )
        )


class SmallCountrySizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.SmallCountry,
            bounds=MapXYBounds(
                lower_bound=ZoomCoordinatesLowerBound.SmallCountry,
                upper_bound=ZoomCoordinatesUpperBound.SmallCountry
            )
        )


class LargeMetropolitanSizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.LargeMetropolitan,
            bounds=MapXYBounds(
                lower_bound=ZoomCoordinatesLowerBound.LargeMetropolitan,
                upper_bound=ZoomCoordinatesUpperBound.LargeMetropolitan
            )
        )


class MetropolitanSizeMap(BaseMap):

    def __init__(self):
        super().__init__(
            area=MapZoom.Metropolitan,
            bounds=MapXYBounds(
                lower_bound=ZoomCoordinatesLowerBound.Metropolitan,
                upper_bound=ZoomCoordinatesUpperBound.Metropolitan
            )
        )
