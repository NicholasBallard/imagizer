FROM python

EXPOSE 80

COPY . /app

RUN pip install -r app/requirements.txt

WORKDIR app/src

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80", "--reload"]