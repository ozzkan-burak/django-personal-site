FROM python:3.10-slim

RUN apt-get update && apt-get install -y python3-dev build-essential libpq-dev

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv VIRTUAL_ENV



# Activate virtual environment and install dependencies
ADD ./requirements.txt /tmp/requirements.txt
RUN VIRTUAL_ENV/bin/pip install -r /tmp/requirements.txt

# Install python-dotenv
RUN /opt/venv/bin/pip install python-dotenv

COPY . /srv/app
WORKDIR /srv/app

