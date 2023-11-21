from abc import ABC, abstractmethod
from io import BytesIO
from PIL import Image
from pathlib import Path
from exceptions import ImageFormatNotAllowed


class ImageSaveInterface(ABC):

    @abstractmethod
    def save_to_file(self, dst_path: Path):
        pass


class MapImage(ImageSaveInterface):

    def __init__(self, image_bytes):
        self._data = bytes()
        self._validate_and_set_image_data(image_bytes)
        self._image = Image.open(BytesIO(self._data))

    def save_to_file(self, dst_path: Path):
        if self._is_desired_save_format_possible(dst_path.suffix):
            self._image.save(dst_path)

    def _is_desired_save_format_possible(self, suffix):
        if self._allowed_image_format() in suffix:
            return True
        else:
            raise ImageFormatNotAllowed(f"Bytes-object allows to save image only as {self._image.format}")

    def _allowed_image_format(self):
        return self._image.format.lower()

    def _validate_and_set_image_data(self, data):
        if isinstance(data, bytes):
            self._data = data
        else:
            raise TypeError("Image data should be type of a bytes-object like")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._validate_and_set_image_data(new_data)
        self._image = Image.open(BytesIO(self._data))


