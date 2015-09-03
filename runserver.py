#!/usr/bin/python
# -*- coding: utf-8 -*- 

from flask import Flask
from flask import request
from flask import render_template

from flask.ext.socketio import SocketIO

import os


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET'] = 'secret!'
app.config['SERVER_NAME'] = os.environ.get('SERVER_NAME')
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message', methods=["POST"])
def message():
    socketio.emit('message', namespace='/test-websockets')
    return 'OK'


@socketio.on('connect', namespace='/test-websockets')
def connected():
    print("Client connected. Namespace: %s" % request.namespace)
    print(request.namespace.socket)
    print(request.namespace.socketio)
    print(request.namespace.session)


if __name__ == '__main__':
    # Don't user the reloader, or sometimes the local development server
    # will hang in the background because of gevent.hub.LoopExit:
    # LoopExit('This operation would block forever',)
    socketio.run(app, use_reloader=False)
