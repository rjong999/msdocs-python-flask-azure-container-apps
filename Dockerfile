# syntax=docker/dockerfile:1

FROM python:3.11.3-slim-buster

WORKDIR /app

RUN pip install flask

RUN pip install flask-restful

COPY requirements.txt requirements.txt

COPY app.py app.py

RUN set FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0"]
