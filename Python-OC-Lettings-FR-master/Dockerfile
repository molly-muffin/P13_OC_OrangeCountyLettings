FROM python:3.11

RUN mkdir /P13_OC_OrangeCountyLettings
WORKDIR /P13_OC_OrangeCountyLettings
COPY . /P13_OC_OrangeCountyLettings
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.oc_lettings_site.settings
CMD ["python", "oc_lettings_site/manage.py", "collectstatic", "--noinput"]
CMD ["gunicorn", "oc_lettings_site.oc_lettings_site.wsgi"]