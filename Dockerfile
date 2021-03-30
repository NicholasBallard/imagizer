FROM tiangolo/uvicorn-gunicorn-fastapi

COPY ./src /app

RUN pip install -r requirements.txt