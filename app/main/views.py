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
    return render_template("MusiCrashTemplates/userCenter.html", async_mode=socketio.async_mode)

@main.route('/testinfo')
def testinfo():
    return render_template("MusiCrashTemplates/userInformation.html", async_mode=socketio.async_mode)

@main.route('/test')
def test():
    return render_template("MusiCrashTemplates/test.html", async_mode=socketio.async_mode)
@main.route('/testmodify')
def testmodify():
    return render_template("MusiCrashTemplates/modifyInfomation.html", async_mode=socketio.async_mode)
