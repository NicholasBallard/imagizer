FROM python

ARG PORT=8080

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src /app/app

WORKDIR /app/app

EXPOSE $PORT

CMD uvicorn main:app --host 0.0.0.0 --port $PORT

# FROM tiangolo/uvicorn-gunicorn-fastapi
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY ./src /app/app
