from typing import Optional
from PIL import Image

from read import read_in_image


def create_favicon(image: Image.Image, pixels: int) -> Optional[Image.Image]:
    dims: tuple[int, int] = image.size
    if not pixels <= min(dims):
        print(
            "Can't upscale a favicon from the original size of {dims} to ({pixels}, {pixels}).".format(
                dims=dims, pixels=pixels
            )
        )
        return
    if dims[0] != dims[1]:
        print(
            "Just warning you this image is not square, so resizing its {dims} is going to look ugly!".format(
                dims=dims
            )
        )
    new_dims: tuple[int, int] = (pixels, pixels)
    # can pad an un-square image with a border color
    return im.resize((pixels, pixels))


def templates():
    pass


def compress():
    pass