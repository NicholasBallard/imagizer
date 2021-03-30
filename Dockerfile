FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip install -r requirements.txt

COPY ./src /app

WORKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port $PORT