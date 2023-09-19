FROM python:3.11

WORKDIR /Python-OC-Lettings-FR-master
COPY . /Python-OC-Lettings-FR-master
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.oc_lettings_site.settings
CMD ["python", "oc_lettings_site/manage.py", "collectstatic", "--noinput"]
CMD ["gunicorn", "oc_lettings_site.oc_lettings_site.wsgi"]