# https://pypi.org/project/qrcode/
# qr is a command line tool for generating QR codes, too!
# qr "Some text" > test.png

from io import BytesIO

from pydantic import (
    BaseModel,
    conint,
)
from fastapi.responses import StreamingResponse
import qrcode

from write import buffer


class QRCodeSettings(BaseModel):
    version: int = 1
    error_correction: conint(gt=-1, lt=4) = 0 # 0-3: error correction level (L,M,Q,H)
    box_size: int = 10
    border: int = 4
    # image_factory: BaseImage
    # mask_pattern: ? = None


def make_qr(value, qr_code_settings: QRCodeSettings) -> qrcode.QRCode:
    qr = qrcode.QRCode(**qr_code_settings.dict())
    qr.add_data(value)
    qr.make(fit=True)
    return qr


# test basic usage
# id = 1
# qr = qrcode.QRCode(
#     version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
# )
# qr.add_data(id)
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")

# # img.show()

# url = "https://imagizer.app/docs"
# qr = qrcode.QRCode(
#     version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
# )
# qr.add_data(url)
# qr.make(fit=True)

# img2 = qr.make_image(fill_color="black", back_color="white")

# # img2.show()

# qr.clear()
# first_qr = 65431
# qr.add_data(first_qr)
# qr.make(fit=True)
# # qr.make_image().show()

# qr.clear()
# second_qr = 65432
# qr.add_data(second_qr)
# qr.make(fit=True)
# # qr.make_image().show()

# # read qr code
# import pyzbar.pyzbar as pyzbar
# from pyzbar.pyzbar import ZBarSymbol
# from PIL import Image

# input_image = Image.open("multi-QR-code.png")

# decoded_objects = pyzbar.decode(input_image, symbols=[ZBarSymbol.QRCODE])

# for obj in decoded_objects:
#     zbarData = obj.data.decode("utf-8")
#     print(zbarData)


def read_qr(image):
    # read from image
    decoded_objects = pyzbar.decode(image, symbols=[ZBarSymbol.QRCODE])
    for obj in decoded_objects:
        zbarData = obj.data.decode("utf-8")
        return zbarData


def read_qr_from_file(file):
    # read from file
    with open(file, "rb") as image:
        return read_qr(image)


# read qr code from video
def read_qr_from_video(video):
    # read from video
    pass


from fastapi import APIRouter


router = APIRouter(
    prefix="/qr", tags=["qr"], responses={404: {"description": "Not Found"}}
)


@router.post("/make")
async def make(value: str, qr_code_settings: QRCodeSettings = QRCodeSettings()):
    qr = make_qr(value, qr_code_settings)
    img = qr.make_image(fill_color="black", back_color="white")
    return StreamingResponse(buffer(img), media_type="image/png")


@router.post("/read")
def read_qr(img):
    pass
