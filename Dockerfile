FROM python

EXPOSE 8080

COPY . /app

RUN pip install -r app/requirements.txt

WORKDIR /app/src

CMD exec uvicorn api:app --host 0.0.0.0