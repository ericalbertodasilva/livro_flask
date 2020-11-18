FROM python:3.9.0

WORKDIR /app

ENV FLASK_ENV=development
ENV FLASK_APP=run.py
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential libffi-dev -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .