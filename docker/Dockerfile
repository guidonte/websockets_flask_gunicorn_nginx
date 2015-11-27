FROM ubuntu:14.04
MAINTAINER Guido Amoruso <guidonte@gmail.com>

RUN apt-get -y update
RUN apt-get -y install python-pip build-essential python-dev python-setuptools
RUN pip install "flask>=0.10" "gevent-socketio==0.3.6" "flask-socketio==0.6.0"

RUN pip install gunicorn==19

WORKDIR /srv/wfgn
