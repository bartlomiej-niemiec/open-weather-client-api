from dataclasses import dataclass


@dataclass(frozen=True)
class MapLayers:
    """Map Layers."""
    clouds: str = "clouds_new"
    precipitation: str = "precipitation_new"
    sea_level_pressure: str = "pressure_new"
    wind_speed: str = "wind_new"
    temperature: str = "temp_new"
