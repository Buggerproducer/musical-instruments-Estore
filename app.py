import uuid
from threading import Lock
from flask import Flask, render_template, session, request, \
    copy_current_request_context, url_for, redirect
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from flask_sqlalchemy import SQLAlchemy
from config import Config

async_mode = None

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
import models
from models import *
from flask_admin import Admin, AdminIndexView, expose




socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()



def background_thread():
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count})


@socketio.event
def my_ping():
    emit('my_pong')


@socketio.event
def join():
    emit("id",{'data':'test'})
    emit("notify",{'data':"someone join"},broadcast=True)

@app.route('/test')
def test():
    return render_template("test_io.html",async_mode=socketio.async_mode)


if __name__ == '__main__':
    socketio.run(app, debug=False, host="0.0.0.0", port=80)
