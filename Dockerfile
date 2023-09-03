FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN apt-get update && \
  apt-get install -y \
  locales \
  locales-all \
  build-essential \
  curl \
  libzbar-dev \
  && pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
  && apt-get clean --dry-run

COPY ./mime.types /etc/mime.types
COPY ./uwsgi.ini /conf/uwsgi.ini
COPY ./courseproject /code

# Start uWSGI
CMD [ "uwsgi", "--ini", "/conf/uwsgi.ini"]