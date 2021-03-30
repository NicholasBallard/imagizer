FROM tiangolo/uvicorn-gunicorn-fastapi

COPY ./src /app

WORKDIR /app

RUN pip install -r requirements.txt