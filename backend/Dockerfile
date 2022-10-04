FROM python:3.8

WORKDIR /app

COPY . /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
#    && apt-get -y install python3-dev\
#                  default-libmysqlclient-dev \
#                  netcat \
    && apt-get -y install netcat \
    && pip install --upgrade pip \
    && pip install -r /app/req.txt

RUN chmod +x /app/scripts/wait_db.sh

