# Dockerfile
FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
RUN mkdir /p13oc_orange_county_lettings
WORKDIR /p13oc_orange_county_lettings
COPY requirements.txt /p13oc_orange_county_lettings/
RUN pip install -r requirements.txt
COPY . /p13oc_orange_county_lettings/