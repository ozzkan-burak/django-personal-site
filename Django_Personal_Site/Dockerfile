FROM python:3.10-slim

# Sistem bağımlılıklarını yükleyin
RUN apt-get update && apt-get install -y python3-dev build-essential libpq-dev

# Ortam değişkenlerini ayarlayın
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# pip'i güncelleyin ve virtualenv'i yükleyin
RUN pip install --upgrade pip
RUN pip install virtualenv

# Sanal ortamı oluşturun
RUN python -m virtualenv $VIRTUAL_ENV

# Gereksinimleri yükleyin
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# python-dotenv'i yükleyin
RUN pip install python-dotenv

# Proje dosyalarını kopyalayın
COPY . /srv/app
WORKDIR /srv/app

# Statik dosyaları toplayın
RUN python manage.py collectstatic --noinput

