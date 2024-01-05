from abc import ABC, abstractmethod
from pathlib import Path


class MapImageInterface(ABC):
    """Interface to manage weather map raw data."""

    @abstractmethod
    def save_to_file(self, dir: Path, filename):
        """save image raw data to file.

        :param dir: directory
        :param filename: name of the image
        """
        pass

    @abstractmethod
    def get_save_format(self):
        """get save of format image.

        :return: name of the format.
        """
        pass

    @abstractmethod
    def get_image_data(self):
        """get image raw data.

        :return: image raw data.
        """
        pass
