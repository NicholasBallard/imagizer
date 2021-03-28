from io import BytesIO
from typing import Union

import requests
from PIL import Image
from pydantic import HttpUrl


def read_in_image(fp: Union[HttpUrl, bytes]) -> Image.Image:
    def read_from_url(url: HttpUrl) -> Image.Image:
        res = requests.get(url)
        image = Image.open(BytesIO(res.content))
        return image

    def read_from_file(fp) -> Image.Image:
        image = Image.open(BytesIO(fp))
        return image

    if isinstance(fp, HttpUrl):
        # TODO test fp is HttpUrl and not just str
        return read_from_url(fp)
    elif isinstance(fp, bytes):
        return read_from_file(fp)
