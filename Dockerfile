FROM --platform=linux/amd64 python:3.11.4-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

RUN apt-get -y install ffmpeg libsm6 libxext6
RUN apt-get -y install tesseract-ocr 

RUN apt-get clean

RUN pip3 install poetry
RUN poetry install

COPY . /usr/src/app