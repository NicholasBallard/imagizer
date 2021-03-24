""" resize.py
"""

from __future__ import annotations
from io import BytesIO
from pathlib import Path
from typing import Union

from PIL import Image
from pydantic import HttpUrl
import requests


"""
Pillow supports lots more:
    https://pillow.readthedocs.io/en/5.1.x/handbook/image-file-formats.html
"""
SUPPORTED_FILE_TYPES: list[str] = [".jpg", ".png"]


def name_file(fp: Path, suffix) -> str:
    return f"{fp.stem}{suffix}{fp.suffix}"


def read_from_url(url: HttpUrl) -> Image:
    res = requests.get(url)
    im: Image = Image.open(BytesIO(res.content))
    return im


def read_from_file(fp) -> Image:
    im: Image = Image.open(BytesIO(fp))
    return im


def resize(fp: Union[str, bytes], scale: Union[float, int]) -> tuple[BytesIO, dict]:
    """ Resize an image maintaining its proportions

    Args:
        fp (str): Path argument to image file
        scale (Union[float, int]): Percent as whole number of original image. eg. 53

    Returns:
        image (np.ndarray): Scaled image
    """
    if isinstance(fp, bytes):
        im: Image = read_from_file(fp)
    else:
        im: Image = read_from_url(fp)
    _scale = lambda dim, s: int(dim * s / 100)
    width, height = im.size
    new_width: int = _scale(width, scale)
    new_height: int = _scale(height, scale)
    new_dim: tuple = (new_width, new_height)
    resized = im.resize(new_dim)
    buf = BytesIO()
    resized.save(buf, format='PNG', quality=100)
    buf.seek(0)
    stats: dict = {
        "orig-width": width,
        "orig-height": height,
        "new-width": new_width,
        "new-height": new_height,
        "scale_pct": scale
    }
    return buf, stats


# salvage what I need for then delete
def main(pattern, scale: int, quiet: bool):
    for image in (images := Path().glob(pattern)):
        if image.suffix not in SUPPORTED_FILE_TYPES:
            continue
        im = resize(image, scale)
        nw, nh = im.size
        suffix: str = f"_{scale}_{nw}x{nh}"
        resize_name: str = name_file(image, suffix)
        _dir: Path = image.absolute().parent
        im.save(_dir / resize_name)
        if not quiet:
            print(
                f"resized image saved to {resize_name}.")
    if images == []:
        print(f"No images found at search pattern '{pattern}'.")
        return
