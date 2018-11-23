FROM python:3.6
ADD . /srv/app
WORKDIR /srv/app
RUN pip3 install -r requirements.txt
CMD uwsgi --ini app.ini