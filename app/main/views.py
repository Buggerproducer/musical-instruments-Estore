import leancloud

from app import socketio
from flask_socketio import SocketIO, emit
from flask import render_template, request, session, jsonify
from . import main
from .forms import LoginForm
from threading import Lock
from leancloud import cloud
from ..utils import product

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


# 索引页面index
@main.route('/')
def index():
    if session.get('authenticated') is None or session.get('authenticated') is False:
        authenticated = False
    else:
        authenticated = True
    return render_template("index.html", authenticated=authenticated, async_mode=socketio.async_mode)


# 登录注册页面
@main.route('/signUp')
def signUp():
    return render_template("signUp.html", async_mode=socketio.async_mode)


# 查看用户登录状态
@main.route('/checkLogin', methods=['POST'])
def checkLogin():
    user = request.form['user']
    if user:
        session['authenticated'] = True
        return jsonify({'response': 1})
    else:
        session['authenticated'] = False
        return jsonify({'response': 2})

# @main.route('/handle-login', methods=['POST'])
# def handle_login():


@main.route('/check', methods=['POST'])
def check():
    print(2)


# 个人信息页面
@main.route('/testbase')
def testbase():
    return render_template("MusiCrashTemplates/userCenter.html", async_mode=socketio.async_mode)


@main.route('/testorder')
def testorder():
    products = product.getAllProduct(0, 50)
    return render_template("test_order.html", products=products, async_mode=socketio.async_mode)


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


# 商品品牌分类页面
@main.route('/category')
def category():
    kinds = product.getAllCategory(0, 50)
    return render_template("category.html", kinds=kinds, async_mode=socketio.async_mode)


@main.route('/products')
def products():
    return render_template("category/steinway.html", async_mode=socketio.async_mode)


# 不同品牌商品的商品展示页面
@main.route('/kind/<kind_id>')
def kinds(kind_id):
    products = product.getProductByCategory(kind_id)
    kind = product.getCategoryById(kind_id)
    return render_template("kind.html", products=products, kind=kind, async_mode=socketio.async_mode)


# 商品具体信息页面
@main.route('/productInfo/<product_id>')
def productInfo(product_id):
    commodity = product.getProductById(product_id)
    # print(product_id)
    # commodity_title = commodity.get('title').get('english')
    return render_template("piano.html", commodity=commodity, async_mode=socketio.async_mode)


@main.route('/testfuwenben')
def testfuwenben():
    return render_template("MusiCrashTemplates/fuwenben.html")


# 后台页面
@main.route('/backend')
def backend():
    return render_template("backend.html")


@main.route('/testCollection')
def testCollection():
    return render_template("MusiCrashTemplates/collectionLists.html")

# @main.route('/grotrian')
# def grotrian():
#     return render_template("category/grotrian.html", async_mode=socketio.async_mode)
#
#
# @main.route('/steinmeyer')
# def steinmeyer():
#     return render_template("category/steinmeyer.html", async_mode=socketio.async_mode)
#
#
# @main.route('/petrof')
# def petrof():
#     return render_template("category/petrof.html", async_mode=socketio.async_mode)
#
#
# @main.route('/yamaha')
# def yamaha():
#     return render_template("category/yamaha.html", async_mode=socketio.async_mode)
#
#
# @main.route('/Bösendorfer')
# def Bösendorfer():
#     return render_template("category/Bösendorfer.html", async_mode=socketio.async_mode)