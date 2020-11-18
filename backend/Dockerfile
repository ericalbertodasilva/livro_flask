FROM python:3.9.0

WORKDIR /code

ENV FLASK_ENV='development'

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["python", "run.py"]