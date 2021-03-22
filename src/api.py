""" api.py

FastAPI
https://fastapi.tiangolo.com/

image resize from file
image resize from url
generate ico files
ml classification of image

"""

from typing import Optional
from io import BytesIO
from json import dumps

from fastapi import FastAPI, File, UploadFile
from PIL import Image
from pydantic import BaseModel, HttpUrl
from starlette.responses import StreamingResponse

from resize import resize


app = FastAPI()

class Image(BaseModel):
    name: Optional[str]
    type: Optional[str]
    file: bytes

@app.post("/fromfile")
async def resize_from_file(file: UploadFile = File(...), scale_pct: float = 50.0):
    image = await file.read()
    resized, headers = resize(image, scale_pct)
    headers.update({
        'orig-filename': file.filename,
        'content-type': file.content_type,
    })
    headers.update({k: str(v) for k, v in headers.items()})
    return StreamingResponse(resized, media_type="image/png", headers=headers)


@app.get("/from_web/{url}/")
async def resize_from_web(url: HttpUrl):
    return {"hi": "person"}

@app.get("/ico/")
async def ico(): pass


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)