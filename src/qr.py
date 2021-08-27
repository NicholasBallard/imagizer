# https://pypi.org/project/qrcode/
# qr is a command line tool for generating QR codes, too!
# qr "Some text" > test.png

import qrcode

# test basic usage
id = 1
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(id)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# img.show()

url = "https://imagizer.app/docs"
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)

img2 = qr.make_image(fill_color="black", back_color="white")

# img2.show()

qr.clear()
first_qr = 65431
qr.add_data(first_qr)
qr.make(fit=True)
qr.make_image().show()

qr.clear()
second_qr = 65432
qr.add_data(second_qr)
qr.make(fit=True)
qr.make_image().show()

# read qr code
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import ZBarSymbol
from PIL import Image

input_image = Image.open("multi-QR-code.png")

decoded_objects = pyzbar.decode(input_image, symbols=[ZBarSymbol.QRCODE])

for obj in decoded_objects:
    zbarData = obj.data.decode("utf-8")
    print(zbarData)


def read_qr(image):
    # read from image
    decoded_objects = pyzbar.decode(image, symbols=[ZBarSymbol.QRCODE])
    for obj in decoded_objects:
        zbarData = obj.data.decode("utf-8")
        return zbarData


def read_qr_from_file(file):
    # read from file
    with open(file, 'rb') as image:
        return read_qr(image)


# read qr code from video
def read_qr_from_video(video):
    # read from video
    pass

