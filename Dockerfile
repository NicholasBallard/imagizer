FROM tiangolo/uvicorn-gunicorn-fastapi

COPY . /app

WORKDIR /app

EXPOSE $PORT

RUN pip install -r requirements.txt