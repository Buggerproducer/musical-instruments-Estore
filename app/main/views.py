from app import socketio
from flask_socketio import SocketIO, emit
from flask import render_template
from . import main
from threading import Lock

thread = None
thread_lock = Lock()


@socketio.event
def my_ping():
    emit('my_pong')


@socketio.event
def join():
    emit("id", {'data':'test'})
    emit("notify", {'data':"someone join"}, broadcast=True)


@main.route('/test')
def test():
    return render_template("test_io.html", async_mode=socketio.async_mode)
