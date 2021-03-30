FROM python

RUN pip install -r requirements.txt

COPY ./src /app

EXPOSE $PORT

CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT