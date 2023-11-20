from dataclasses import dataclass
from io import BytesIO
import requests
from PIL import Image
from pathlib import Path


@dataclass(frozen=True)
class Format:
    JPG = "jpg"
    PNG = "png"


class MapImageSaver:

    @staticmethod
    def save(api_request_response: requests.Response, dst_path: str, name: str, format: str):
        image = Image.open(BytesIO(api_request_response.text))
        path = Path(dst_path, name).with_suffix(format)
        image.save(path)
