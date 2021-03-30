FROM tiangolo/uvicorn-gunicorn-fastapi

COPY . /app

WORKDIR /app/src