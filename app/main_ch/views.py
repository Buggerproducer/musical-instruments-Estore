from app import socketio
from flask_socketio import SocketIO, emit
from flask import render_template, request, session, jsonify, redirect, url_for
from . import ch
from threading import Lock
from functools import wraps
from leancloud import cloud
from ..utils import product, user

thread = None
thread_lock = Lock()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('authenticated') is None or session.get('authenticated') is False:
            return redirect(url_for("main.signUp"))
        return f(*args, **kwargs)
    return decorated_function


# 索引页面index
@ch.route('/')
def index():
    if session.get('authenticated') is None or session.get('authenticated') is False:
        authenticated = False
    else:
        authenticated = True
    return render_template("index_zh.html", authenticated=authenticated, async_mode=socketio.async_mode)


# 登录注册页面
@ch.route('/signUp')
def signUp():
    return render_template("signUp_zh.html", async_mode=socketio.async_mode)


# 个人信息页面
@ch.route('/testbase')
def testbase():
    return render_template("MusiCrashTemplates/userCenter_zh.html", async_mode=socketio.async_mode)


@ch.route('/testinfo')
def testinfo():
    return render_template("MusiCrashTemplates/userInformation_zh.html", async_mode=socketio.async_mode)


@ch.route('/testmodify')
def testmodify():
    return render_template("MusiCrashTemplates/modifyInfomation_zh.html", async_mode=socketio.async_mode)


# 商品品牌分类页面
@ch.route('/category')
def category():
    kinds = product.getAllCategory(0, 50)
    return render_template("category_zh.html", kinds=kinds, async_mode=socketio.async_mode)


# 不同品牌商品的商品展示页面
@ch.route('/kind/<kind_id>')
def kinds(kind_id):
    products = product.getProductByCategory(kind_id)
    kind = product.getCategoryById(kind_id)
    return render_template("kind_zh.html", products=products, kind=kind, async_mode=socketio.async_mode)


# 商品具体信息页面
@ch.route('/productInfo/<product_id>')
def productInfo(product_id):
    commodity = product.getProductById(product_id, record=True)
    # print(product_id)
    # commodity_title = commodity.get('title').get('english')
    return render_template("piano_zh.html", commodity=commodity, async_mode=socketio.async_mode)
