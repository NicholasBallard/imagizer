FROM python

EXPOSE $PORT

COPY . /app

RUN pip install -r app/requirements.txt

WORKDIR /app/src

CMD exec uvicorn api:app --host 0.0.0.0 --port $PORT