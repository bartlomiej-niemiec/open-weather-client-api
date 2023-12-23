from src.WeatherMapsClient.constants import MapZoom
import src.WeatherMapsClient.Maps as MapArea
from src.WeatherMapsClient.exceptions import UnsupportedZoomLevel


class MapParametersFactory:
    LOWER_ZOOM_LEVEL = 0
    GREATEST_ZOOM_LEVEL = 9

    @staticmethod
    def create(map_area: int):
        if map_area == MapZoom.Worldwide:
            return MapArea.WorldwideSizeMap()
        elif map_area == MapZoom.OneQuarterOfTheWorld:
            return MapArea.OneQuarterOfTheWorldSizeMap()
        elif map_area == MapZoom.Subcontinental:
            return MapArea.SubcontinentalSizeMap()
        elif map_area == MapZoom.LargestCountry:
            return MapArea.LargestCountryeMap()
        elif map_area == MapZoom.LargestAsiaCountry:
            return MapArea.LargestAsiaCountrySizeMap()
        elif map_area == MapZoom.LargeAfricanCountry:
            return MapArea.LargeAfricanCountrySizeMap()
        elif map_area == MapZoom.LargeEuropeanCountry:
            return MapArea.LargeEuropeanCountrySizeMap()
        elif map_area == MapZoom.SmallCountry:
            return MapArea.SmallCountrySizeMap()
        elif map_area == MapZoom.LargeMetropolitan:
            return MapArea.LargeMetropolitanSizeMap()
        elif map_area == MapZoom.Metropolitan:
            return MapArea.MetropolitanSizeMap()
        else:
            raise UnsupportedZoomLevel(f"Given zoom level is not possible.",
                                       f"Zoom level should be in range {MapParametersFactory.LOWER_ZOOM_LEVEL}"
                                       f"to {MapParametersFactory.GREATEST_ZOOM_LEVEL}")
