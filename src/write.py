from io import BytesIO


def buffer(image_file) -> BytesIO:
    buffer = BytesIO()
    # TODO inflect format
    image_file.save(buffer, format="PNG", quality=100)
    buffer.seek(0)
    return buffer