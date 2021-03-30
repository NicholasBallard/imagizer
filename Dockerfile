FROM python

ENV PORT 8080

EXPOSE 8080

COPY . /app

RUN pip install -r app/requirements.txt

WORKDIR /app/src

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]