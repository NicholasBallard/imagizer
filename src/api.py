""" api.py

FastAPI
https://fastapi.tiangolo.com/

image resize from file **DONE**
image resize from url **DONE**
generate ico files 
ml classification of image 
access: google drive, onedrive, dropbox, s3 
save in s3 bucket 


"""

from typing import Optional
from io import BytesIO
from json import dumps

from fastapi import FastAPI, File, UploadFile
from fastapi.openapi.utils import get_openapi
from PIL import Image
from pydantic import BaseModel, HttpUrl
from starlette.responses import StreamingResponse

from resize import resize


app = FastAPI()


def custom_openapi() -> dict:
    """Get the OpenAPI spec

    Ref:
        https://fastapi.tiangolo.com/advanced/extending-openapi/#extending-openapi

    Returns:
        dict: The OpenAPI spec
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Imagizer API",
        version="0.0.1",
        description="Image manipulation service.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.post("/resize-file")
async def resize_from_file(file: UploadFile = File(...), scale_pct: float = 50.0):
    image = await file.read()
    resized, headers = resize(image, scale_pct)
    headers.update(
        {
            "orig-filename": file.filename,
            "content-type": file.content_type,
        }
    )
    headers.update({k: str(v) for k, v in headers.items()})
    return StreamingResponse(resized, media_type="image/png", headers=headers)


@app.get("/resize-url")
async def resize_from_url(url: HttpUrl, scale_pct: float = 50.0):
    resized, headers = resize(url, scale_pct)
    headers.update({k: str(v) for k, v in headers.items()})
    return StreamingResponse(resized, media_type="image/png", headers=headers)


@app.post("/favicon")
async def favicon(image) -> list[bytes]:
    """Favicon generator from an image.

    Ref:
        - https://www.emergeinteractive.com/insights/detail/the-essentials-of-favicons/
        - https://www.creativebloq.com/illustrator/create-perfect-favicon-12112760
        - https://www.tutorialspoint.com/What-are-favicon-best-practices-regarding-size-and-format

    | **Size** | **Name**        | **Purpose**                                                  |
    | -------- | --------------- | ------------------------------------------------------------ |
    | 32×32    | favicon-32.png  | Standard for most desktop browsers                           |
    | 128×128  | favicon-128.png | Chrome Web Store icon & Small Windows 8 Star Screen Icon*    |
    | 152×152  | favicon-152.png | iPad touch icon (Change for iOS 7: up from 144×144)          |
    | 167×167  | favicon-167.png | iPad Retina touch icon                                       |
    | 180×180  | favicon-180.png | iPhone Retina                                                |
    | 192×192  | favicon-192.png | Google Developer Web App Manifest Recommendation             |
    | 196×196  | favicon-196.png | Chrome for Android home screen icon                          |

    For each of the favicons above, have two versions:
        1. transparent background
        2. solid fill background

    README.txt included in response.
        - Explain what each size is for.

    SNIPPET.html
        - Example HTML code for including the favicons on a website.

    Args:
        image ([type]): [description]

    Returns:
        list[bytes]: [description]
    """
    sizes: list[tuple[int, int]] = [(x, x) for x in [32, 128, 152, 167, 180, 192, 196]]
    name_file = lambda size: f"favicon-{size}.png"



if __name__ == "__main__":
    # debugging
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
