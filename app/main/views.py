import leancloud

from app import socketio
from flask_socketio import SocketIO, emit
from flask import render_template
from . import main
from .forms import LoginForm
from threading import Lock
from leancloud import cloud

# leancloud.init("pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI", "pShwYQQ4JVfSStc56MvkHNrr")

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


@main.route('/signUp')
def signUp():
    return render_template("signUp.html", async_mode=socketio.async_mode)


# @main.route('/handle-login', methods=['POST'])
# def handle_login():



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


@main.route('/testmodifypw')
def testmodifypw():
    return render_template("MusiCrashTemplates/re.html", async_mode=socketio.async_mode)


@main.route('/category')
def category():
    return render_template("category.html", async_mode=socketio.async_mode)


@main.route('/products')
def products():
    return render_template("category/steinway.html", async_mode=socketio.async_mode)

@main.route('/grotrian')
def grotrian():
    return render_template("category/grotrian.html", async_mode=socketio.async_mode)


@main.route('/productInfo')
def productInfo():
    return render_template("piano1.html", async_mode=socketio.async_mode)

