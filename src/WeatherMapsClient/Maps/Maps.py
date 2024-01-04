from src.WeatherMapsClient.Maps.MapsConstants import MapZoom, ZoomCoordinatesLowerBound, ZoomCoordinatesUpperBound
from src.WeatherMapsClient.Maps.MapBoundsChecker import MapBoundsChecker
from src.WeatherMapsClient.Maps.BaseMapWithBoundChecker import BaseMapWithBoundsChecking


class WorldwideSizeMap(BaseMapWithBoundsChecking):

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.Worldwide,
            bounds_checker=MapBoundsChecker(
                lower_bound=ZoomCoordinatesLowerBound.Worldwide,
                upper_bound=ZoomCoordinatesUpperBound.Worldwide
            )
        )


class OneQuarterOfTheWorldSizeMap(BaseMapWithBoundsChecking):

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.OneQuarterOfTheWorld,
            bounds_checker=MapBoundsChecker(
                lower_bound=ZoomCoordinatesLowerBound.OneQuarterOfTheWorld,
                upper_bound=ZoomCoordinatesUpperBound.OneQuarterOfTheWorld
            )
        )


class SubcontinentalSizeMap(BaseMapWithBoundsChecking):

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.Subcontinental,
            bounds_checker=MapBoundsChecker(
                lower_bound=ZoomCoordinatesLowerBound.Subcontinental,
                upper_bound=ZoomCoordinatesUpperBound.Subcontinental
            )
        )


class LargestCountryeMap(BaseMapWithBoundsChecking):

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.LargestCountry,
            bounds_checker=MapBoundsChecker(
                lower_bound=ZoomCoordinatesLowerBound.LargestCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargestCountry
            )
        )


class LargestAsiaCountrySizeMap(BaseMapWithBoundsChecking):

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.LargestAsiaCountry,
            bounds_checker=MapBoundsChecker(
                lower_bound=ZoomCoordinatesLowerBound.LargestAsiaCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargestAsiaCountry
            )
        )


class LargeAfricanCountrySizeMap(BaseMapWithBoundsChecking):

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.LargeAfricanCountry,
            bounds_checker=MapBoundsChecker(
                lower_bound=ZoomCoordinatesLowerBound.LargeAfricanCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargeAfricanCountry
            )
        )


class LargeEuropeanCountrySizeMap(BaseMapWithBoundsChecking):

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.LargeEuropeanCountry,
            bounds_checker=MapBoundsChecker(
                lower_bound=ZoomCoordinatesLowerBound.LargeEuropeanCountry,
                upper_bound=ZoomCoordinatesUpperBound.LargeEuropeanCountry
            )
        )


class SmallCountrySizeMap(BaseMapWithBoundsChecking):

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.SmallCountry,
            bounds_checker=MapBoundsChecker(
                lower_bound=ZoomCoordinatesLowerBound.SmallCountry,
                upper_bound=ZoomCoordinatesUpperBound.SmallCountry
            )
        )


class LargeMetropolitanSizeMap(BaseMapWithBoundsChecking):

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.LargeMetropolitan,
            bounds_checker=MapBoundsChecker(
                lower_bound=ZoomCoordinatesLowerBound.LargeMetropolitan,
                upper_bound=ZoomCoordinatesUpperBound.LargeMetropolitan
            )
        )


class MetropolitanSizeMap(BaseMapWithBoundsChecking):

    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.Metropolitan,
            bounds_checker=MapBoundsChecker(
                lower_bound=ZoomCoordinatesLowerBound.Metropolitan,
                upper_bound=ZoomCoordinatesUpperBound.Metropolitan
            )
        )
