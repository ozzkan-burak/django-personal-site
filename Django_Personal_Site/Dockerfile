FROM python:3.10-slim

RUN apt-get update

RUN apt-get install python3-dev build-essential -y

#pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv /opt/venv

ADD ./requirements.txt /tmp/requirements.txt

COPY . /srv/app
WORKDIR /srv/app
