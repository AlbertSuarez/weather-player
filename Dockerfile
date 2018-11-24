FROM python:3.6
ADD . /srv/app
WORKDIR /srv/app
RUN pip3 install -r requirements.txt
RUN apt-get install python3-tk
CMD uwsgi --ini player.ini