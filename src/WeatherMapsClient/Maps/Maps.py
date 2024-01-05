from src.WeatherMapsClient.Maps.MapsConstants import MapZoom, XYCoordinatesLowerBound, XYCoordinatesUpperBound
from src.WeatherMapsClient.Maps.MapBoundsChecker import MapBoundsChecker
from src.WeatherMapsClient.Maps.MapCoordinatesWithBoundChecker import MapCoordinatesWithBoundsChecking


class WorldwideSizeMap(MapCoordinatesWithBoundsChecking):
    """Map Size corresponding to the size of whole World."""
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.Worldwide,
            bounds_checker=MapBoundsChecker(
                lower_bound=XYCoordinatesLowerBound.Worldwide,
                upper_bound=XYCoordinatesUpperBound.Worldwide
            )
        )


class OneQuarterOfTheWorldSizeMap(MapCoordinatesWithBoundsChecking):
    """Map Size corresponding to the size of One Quarter of the World."""
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.OneQuarterOfTheWorld,
            bounds_checker=MapBoundsChecker(
                lower_bound=XYCoordinatesLowerBound.OneQuarterOfTheWorld,
                upper_bound=XYCoordinatesUpperBound.OneQuarterOfTheWorld
            )
        )


class SubcontinentalSizeMap(MapCoordinatesWithBoundsChecking):
    """Map Size corresponding to the size of Subcontinental."""
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.Subcontinental,
            bounds_checker=MapBoundsChecker(
                lower_bound=XYCoordinatesLowerBound.Subcontinental,
                upper_bound=XYCoordinatesUpperBound.Subcontinental
            )
        )


class LargestCountrySizeMap(MapCoordinatesWithBoundsChecking):
    """Map Size corresponding to the size of the Largest Country in the World."""
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.LargestCountry,
            bounds_checker=MapBoundsChecker(
                lower_bound=XYCoordinatesLowerBound.LargestCountry,
                upper_bound=XYCoordinatesUpperBound.LargestCountry
            )
        )


class LargestAsiaCountrySizeMap(MapCoordinatesWithBoundsChecking):
    """Map Size corresponding to the size of the Largest Asia Country."""
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.LargestAsiaCountry,
            bounds_checker=MapBoundsChecker(
                lower_bound=XYCoordinatesLowerBound.LargestAsiaCountry,
                upper_bound=XYCoordinatesUpperBound.LargestAsiaCountry
            )
        )


class LargeAfricanCountrySizeMap(MapCoordinatesWithBoundsChecking):
    """Map Size corresponding to the size of the Largest African Country."""
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.LargeAfricanCountry,
            bounds_checker=MapBoundsChecker(
                lower_bound=XYCoordinatesLowerBound.LargeAfricanCountry,
                upper_bound=XYCoordinatesUpperBound.LargeAfricanCountry
            )
        )


class LargeEuropeanCountrySizeMap(MapCoordinatesWithBoundsChecking):
    """Map Size corresponding to the size of the Largest European Country."""
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.LargeEuropeanCountry,
            bounds_checker=MapBoundsChecker(
                lower_bound=XYCoordinatesLowerBound.LargeEuropeanCountry,
                upper_bound=XYCoordinatesUpperBound.LargeEuropeanCountry
            )
        )


class SmallCountrySizeMap(MapCoordinatesWithBoundsChecking):
    """Map Size corresponding to the size of the Small Country."""
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.SmallCountry,
            bounds_checker=MapBoundsChecker(
                lower_bound=XYCoordinatesLowerBound.SmallCountry,
                upper_bound=XYCoordinatesUpperBound.SmallCountry
            )
        )


class LargeMetropolitanSizeMap(MapCoordinatesWithBoundsChecking):
    """Map Size corresponding to the size of the Large Metropolitan."""
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.LargeMetropolitan,
            bounds_checker=MapBoundsChecker(
                lower_bound=XYCoordinatesLowerBound.LargeMetropolitan,
                upper_bound=XYCoordinatesUpperBound.LargeMetropolitan
            )
        )


class MetropolitanSizeMap(MapCoordinatesWithBoundsChecking):
    """Map Size corresponding to the size of the Metropolitan."""
    def __init__(self, x, y):
        super().__init__(
            x=x,
            y=y,
            z=MapZoom.Metropolitan,
            bounds_checker=MapBoundsChecker(
                lower_bound=XYCoordinatesLowerBound.Metropolitan,
                upper_bound=XYCoordinatesUpperBound.Metropolitan
            )
        )
