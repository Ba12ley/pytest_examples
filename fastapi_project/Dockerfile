FROM python:3.11.0-alpine

WORKDIR /fastapi_project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY requirements.txt /fastapi_project/requirements.txt

RUN apk update && apk add bash
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


# copy project
COPY . /fastapi_project
EXPOSE 8000