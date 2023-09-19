# Dockerfile
FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
RUN mkdir /oc_p13_lettings
WORKDIR /oc_p13_lettings
COPY requirements.txt /oc_p13_lettings/
RUN pip install -r requirements.txt
COPY Python-OC-Lettings-FR-master/ /oc_p13_lettings/