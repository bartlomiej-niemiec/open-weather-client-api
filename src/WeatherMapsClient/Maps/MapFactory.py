from src.WeatherMapsClient.Maps.MapsConstants import MapZoom, ZoomCoordinatesLowerBound, ZoomCoordinatesUpperBound
import src.WeatherMapsClient.Maps.Maps as MapArea
from src.WeatherMapsClient.Exceptions import UnsupportedZoomLevel


class MapFactory:
    LOWER_ZOOM_LEVEL = 0
    GREATEST_ZOOM_LEVEL = 9

    @staticmethod
    def create(map_area: int):
        if map_area == MapZoom.Worldwide:
            middle_point = (ZoomCoordinatesLowerBound.Worldwide + ZoomCoordinatesUpperBound.Worldwide) // 2
            return MapArea.WorldwideSizeMap(x=middle_point, y=middle_point)
        elif map_area == MapZoom.OneQuarterOfTheWorld:
            middle_point = (ZoomCoordinatesLowerBound.OneQuarterOfTheWorld + ZoomCoordinatesUpperBound.OneQuarterOfTheWorld) // 2
            return MapArea.OneQuarterOfTheWorldSizeMap(x=middle_point, y=middle_point)
        elif map_area == MapZoom.Subcontinental:
            middle_point = (ZoomCoordinatesLowerBound.Subcontinental + ZoomCoordinatesUpperBound.Subcontinental) // 2
            return MapArea.SubcontinentalSizeMap(x=middle_point, y=middle_point)
        elif map_area == MapZoom.LargestCountry:
            middle_point = (ZoomCoordinatesLowerBound.LargestCountry + ZoomCoordinatesUpperBound.LargestCountry) // 2
            return MapArea.LargestCountryeMap(x=middle_point, y=middle_point)
        elif map_area == MapZoom.LargestAsiaCountry:
            middle_point = (ZoomCoordinatesLowerBound.LargestAsiaCountry + ZoomCoordinatesUpperBound.LargestAsiaCountry) // 2
            return MapArea.LargestAsiaCountrySizeMap(x=middle_point, y=middle_point)
        elif map_area == MapZoom.LargeAfricanCountry:
            middle_point = (ZoomCoordinatesLowerBound.LargeAfricanCountry + ZoomCoordinatesUpperBound.LargeAfricanCountry) // 2
            return MapArea.LargeAfricanCountrySizeMap(x=middle_point, y=middle_point)
        elif map_area == MapZoom.LargeEuropeanCountry:
            middle_point = (ZoomCoordinatesLowerBound.LargeEuropeanCountry + ZoomCoordinatesUpperBound.LargeEuropeanCountry) // 2
            return MapArea.LargeEuropeanCountrySizeMap(x=middle_point, y=middle_point)
        elif map_area == MapZoom.SmallCountry:
            middle_point = (ZoomCoordinatesLowerBound.SmallCountry + ZoomCoordinatesUpperBound.SmallCountry) // 2
            return MapArea.SmallCountrySizeMap(x=middle_point, y=middle_point)
        elif map_area == MapZoom.LargeMetropolitan:
            middle_point = (ZoomCoordinatesLowerBound.LargeMetropolitan + ZoomCoordinatesUpperBound.LargeMetropolitan) // 2
            return MapArea.LargeMetropolitanSizeMap(x=middle_point, y=middle_point)
        elif map_area == MapZoom.Metropolitan:
            middle_point = (ZoomCoordinatesLowerBound.Metropolitan + ZoomCoordinatesUpperBound.Metropolitan) // 2
            return MapArea.MetropolitanSizeMap(x=middle_point, y=middle_point)
        else:
            raise UnsupportedZoomLevel(f"Given zoom level is not possible.",
                                       f"Zoom level should be in range {MapFactory.LOWER_ZOOM_LEVEL}"
                                       f"to {MapFactory.GREATEST_ZOOM_LEVEL}")
