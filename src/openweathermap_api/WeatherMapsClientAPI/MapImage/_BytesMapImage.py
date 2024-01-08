from io import BytesIO
from PIL import Image
from pathlib import Path
from src.openweathermap_api.WeatherMapsClientAPI.MapImage._MapImage import MapImageInterface


class BytesMapImage(MapImageInterface):
    """Manipulate image data - bytes."""

    def __init__(self, image_bytes: bytes):
        """Initialize object.

        :param image_bytes: bytes object contains image data.
        """
        if isinstance(image_bytes, bytes):
            self._image = Image.open(BytesIO(image_bytes))
            self._image_data = image_bytes
        else:
            raise TypeError("Image data should be type of a bytes-object like")

    def save_to_file(self, dir: Path, filename: str):
        """save to file under passed localization and filename.

        :param dir: directory.
        :param filename: name of the image.
        """
        filename_with_suffix = filename + self._image.format
        save_path = dir.joinpath(filename_with_suffix)
        self._image.save(save_path)

    def get_save_format(self):
        """get save format of a file based on image data.

        :return: save format.
        """
        return self._image.format

    def get_image_data(self):
        """get bytes object.

        :return: image bytes object.
        """
        return self._image_data

