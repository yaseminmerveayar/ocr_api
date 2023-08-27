FROM python:3.11

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN apt-get update \
    && apt-get -y install tesseract-ocr 


RUN pip3 install poetry
RUN poetry install

COPY . /app