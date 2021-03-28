""" resize.py
"""

from __future__ import annotations
from io import BytesIO
from pathlib import Path
from typing import Union

from PIL import Image
from pydantic import HttpUrl

from read import read_in_image


def resize(image: Union[HttpUrl, bytes], scale: Union[float, int]) -> tuple[BytesIO, dict]:
    """Resize an image maintaining its proportions

    Args:
        fp (str): Path argument to image file
        scale (Union[float, int]): Percent as whole number of original image. eg. 53

    Returns:
        image (np.ndarray): Scaled image
    """
    im: Image.Image = read_in_image(image)
    _scale = lambda dim, s: int(dim * s / 100)
    width, height = im.size
    new_width: int = _scale(width, scale)
    new_height: int = _scale(height, scale)
    new_dim: tuple = (new_width, new_height)
    resized = im.resize(new_dim)
    buf = BytesIO()
    resized.save(buf, format="PNG", quality=100)
    buf.seek(0)
    stats: dict = {
        "orig-width": width,
        "orig-height": height,
        "new-width": new_width,
        "new-height": new_height,
        "scale_pct": scale,
    }
    return buf, stats
