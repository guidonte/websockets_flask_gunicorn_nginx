#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="Websocketxi/Flask Gunicorn/Nginx",
    version="0.1",
    description="Show deployment of a Flask/Websocket application with Docker",
    packages=find_packages(),
    install_requires=[
        "flask>=0.10",
        "gevent-socketio==0.3.6",
        "flask-socketio==0.6.0",
    ],
)
