# FROM python

# RUN pip install -r requirements.txt

# COPY . /app

# EXPOSE $PORT

# WORKDIR /app/src

# CMD uvicorn main:app --host 0.0.0.0 --port $PORT

FROM tiangolo/uvicorn-gunicorn-fastapi
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src /app/app
