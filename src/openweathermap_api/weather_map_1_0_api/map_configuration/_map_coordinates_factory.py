from src.openweathermap_api.weather_map_1_0_api.map_configuration._maps_constants import MapZoom, XYCoordinatesLowerBound, XYCoordinatesUpperBound
from src.openweathermap_api.weather_map_1_0_api.map_configuration._concrete_maps import LargestAsiaCountrySizeMap, \
    LargeEuropeanCountrySizeMap, SubcontinentalSizeMap, LargeMetropolitanSizeMap, OneQuarterOfTheWorldSizeMap, \
    SmallCountrySizeMap, LargeAfricanCountrySizeMap, WorldwideSizeMap, MetropolitanSizeMap, LargestCountrySizeMap
from src.openweathermap_api.weather_map_1_0_api.map_configuration._map_exceptions import UnsupportedZoomLevel


class MapCoordinatesFactory:
    """MapCoordinates Factory."""
    LOWER_ZOOM_LEVEL = 0
    GREATEST_ZOOM_LEVEL = 9

    @staticmethod
    def create(z: int):
        """"Create MapCoordinates with default value based on passed zoom level.

        :param z: z/zoom_level coordinate value
        :return:
        """
        if z == MapZoom.Worldwide:
            middle_point = (XYCoordinatesLowerBound.Worldwide + XYCoordinatesUpperBound.Worldwide) // 2
            return WorldwideSizeMap(x=middle_point, y=middle_point)
        elif z == MapZoom.OneQuarterOfTheWorld:
            middle_point = (XYCoordinatesLowerBound.OneQuarterOfTheWorld + XYCoordinatesUpperBound.OneQuarterOfTheWorld) // 2
            return OneQuarterOfTheWorldSizeMap(x=middle_point, y=middle_point)
        elif z == MapZoom.Subcontinental:
            middle_point = (XYCoordinatesLowerBound.Subcontinental + XYCoordinatesUpperBound.Subcontinental) // 2
            return SubcontinentalSizeMap(x=middle_point, y=middle_point)
        elif z == MapZoom.LargestCountry:
            middle_point = (XYCoordinatesLowerBound.LargestCountry + XYCoordinatesUpperBound.LargestCountry) // 2
            return LargestCountrySizeMap(x=middle_point, y=middle_point)
        elif z == MapZoom.LargestAsiaCountry:
            middle_point = (XYCoordinatesLowerBound.LargestAsiaCountry + XYCoordinatesUpperBound.LargestAsiaCountry) // 2
            return LargestAsiaCountrySizeMap(x=middle_point, y=middle_point)
        elif z == MapZoom.LargeAfricanCountry:
            middle_point = (XYCoordinatesLowerBound.LargeAfricanCountry + XYCoordinatesUpperBound.LargeAfricanCountry) // 2
            return LargeAfricanCountrySizeMap(x=middle_point, y=middle_point)
        elif z == MapZoom.LargeEuropeanCountry:
            middle_point = (XYCoordinatesLowerBound.LargeEuropeanCountry + XYCoordinatesUpperBound.LargeEuropeanCountry) // 2
            return LargeEuropeanCountrySizeMap(x=middle_point, y=middle_point)
        elif z == MapZoom.SmallCountry:
            middle_point = (XYCoordinatesLowerBound.SmallCountry + XYCoordinatesUpperBound.SmallCountry) // 2
            return SmallCountrySizeMap(x=middle_point, y=middle_point)
        elif z == MapZoom.LargeMetropolitan:
            middle_point = (XYCoordinatesLowerBound.LargeMetropolitan + XYCoordinatesUpperBound.LargeMetropolitan) // 2
            return LargeMetropolitanSizeMap(x=middle_point, y=middle_point)
        elif z == MapZoom.Metropolitan:
            middle_point = (XYCoordinatesLowerBound.Metropolitan + XYCoordinatesUpperBound.Metropolitan) // 2
            return MetropolitanSizeMap(x=middle_point, y=middle_point)
        else:
            raise UnsupportedZoomLevel(f"Given zoom level is not possible.",
                                       f"Zoom level should be in range {MapCoordinatesFactory.LOWER_ZOOM_LEVEL}"
                                       f"to {MapCoordinatesFactory.GREATEST_ZOOM_LEVEL}")
