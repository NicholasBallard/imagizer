from fastapi import FastAPI
from pyzbar.pyzbar import decode
from PIL import Image


router = FastAPI()

@router.get("/barcode/{image}")
def barcode_decode(img):
    barcodes = decode(img)
    data = {"barcodes": {}}
    for ix, barcode in enumerate(barcodes):
        data["barcodes"][ix+1] = {"type": barcode.type, "data": barcode.data.decode("utf-8")}
    return data

img = Image.open('barcode_1059313.jpg')
barcodes = barcode_decode(img)
barcodes