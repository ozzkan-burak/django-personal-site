FROM python:3.10-slim

RUN apt-get update && apt-get install -y python3-dev build-essential libpq-dev

# pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

# Activate virtual environment and install dependencies
ADD ./requirements.txt /tmp/requirements.txt
RUN /opt/venv/bin/pip install -r /tmp/requirements.txt

# Install python-dotenv
RUN /opt/venv/bin/pip install python-dotenv

COPY . /srv/app
WORKDIR /srv/app

