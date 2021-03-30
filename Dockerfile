FROM python

COPY . /app

WORKDIR /app

EXPOSE $PORT

RUN pip install -r requirements.txt

CMD uvicorn src.api:app --host 0.0.0.0