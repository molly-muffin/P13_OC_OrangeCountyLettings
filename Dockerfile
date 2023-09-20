FROM python:3-alpine

ENV PYTHONUNBUFFERED 1
ENV PORT 8000

RUN mkdir /oc_p13_lettings
WORKDIR /oc_p13_lettings

COPY requirements.txt /oc_p13_lettings/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /oc_p13_lettings/

CMD python manage.py runserver 127.0.0.1:$PORT