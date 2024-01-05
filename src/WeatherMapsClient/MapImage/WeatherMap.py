from io import BytesIO
from PIL import Image
from pathlib import Path
from src.WeatherMapsClient.MapImage.MapImage import MapImageInterface


class BytesMapImage(MapImageInterface):

    def __init__(self, image_bytes):
        if isinstance(image_bytes, bytes):
            self._image = Image.open(BytesIO(image_bytes))
            self._image_data = image_bytes
        else:
            raise TypeError("Image data should be type of a bytes-object like")

    def save_to_file(self, dir: Path, filename: str):
        filename_with_suffix = filename + self._image.format
        save_path = dir.joinpath(filename_with_suffix)
        self._image.save(save_path)

    def get_save_format(self):
        return self._image.format

    def get_image_data(self):
        return self._image_data

