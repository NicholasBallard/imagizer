FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip install -r requirements.txt

COPY ./src /app

