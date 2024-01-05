from abc import ABC, abstractmethod
from pathlib import Path


class MapImageInterface(ABC):

    @abstractmethod
    def save_to_file(self, dir: Path, filename):
        pass

    @abstractmethod
    def get_save_format(self):
        pass

    @abstractmethod
    def get_image_data(self):
        pass
