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


@main.route('/testio')
def testio():
    return render_template("test_io.html", async_mode=socketio.async_mode)


@main.route('/testlogin')
def testlogin():
    return render_template("test_login.html", async_mode=socketio.async_mode)


@main.route('/')
def index():
    return render_template("index.html", async_mode=socketio.async_mode)

@main.route('/testbase')
def testbase():
    return render_template("MusiCrashTemplates/userInfo.html",async_mode=socketio.async_mode)

