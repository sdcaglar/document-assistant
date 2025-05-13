FROM python:3.10

WORKDIR /app

COPY requirements.txt .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

