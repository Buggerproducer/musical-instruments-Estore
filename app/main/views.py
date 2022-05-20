import leancloud

import app
from app import socketio
from flask_socketio import SocketIO, emit
from flask import render_template, request, session, jsonify, redirect, url_for

from . import main
from .forms import LoginForm
from threading import Lock
from functools import wraps
from leancloud import cloud
from ..utils import product, user

from flask import Flask
app=Flask(__name__)
from werkzeug.utils import import_string
import werkzeug
werkzeug.import_string = import_string
from flask_cache import Cache
cache = Cache(app, config={'CACHE_TYPE':'simple'})


# leancloud.init("pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI", "pShwYQQ4JVfSStc56MvkHNrr")
thread = None
thread_lock = Lock()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('authenticated') is None or session.get('authenticated') is False:
            return redirect(url_for("main.signUp"))
        return f(*args, **kwargs)
    return decorated_function


@socketio.event
def my_ping():
    emit('my_pong')


@socketio.event
def join():
    emit("id", {'data':'test'})
    emit("notify", {'data':"someone join"}, broadcast=True)


# 索引页面index_zh
@main.route('/')
@cache.cached(timeout=300)
def index():
    kinds = product.getAllCategory(0, 50)
    print(1)
    if session.get('authenticated') is None or session.get('authenticated') is False:
        authenticated = False
    else:
        authenticated = True
    return render_template("index_en.html", kinds=kinds, authenticated=authenticated, async_mode=socketio.async_mode)


# 登录注册页面
@main.route('/signUp')
def signUp():
    return render_template("signUp_en.html", async_mode=socketio.async_mode)


# 查看用户登录状态
@main.route('/checkLogin', methods=['POST'])
def checkLogin():
    user = request.form['user']
    print(user)
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
    return render_template("MusiCrashTemplates/userCenter_en.html", async_mode=socketio.async_mode)


@main.route('/history_order')
def history_order():
    return render_template("MusiCrashTemplates/orderList.html", async_mode=socketio.async_mode)


@main.route('/collection/<user_id>')
def collection(user_id):
    collections = user.getCollectionByUser(user_id)
    return render_template("MusiCrashTemplates/collectionLists.html", collections=collections, async_mode=socketio.async_mode)


@main.route('/testinfo')
def testinfo():
    return render_template("MusiCrashTemplates/userInformation_en.html", async_mode=socketio.async_mode)




@main.route('/testmodify')
def testmodify():
    return render_template("MusiCrashTemplates/modifyInfomation_en.html", async_mode=socketio.async_mode)


# 商品品牌分类页面
@main.route('/category')
def category():
    kinds = product.getAllCategory(0, 50)
    return render_template("category_en.html", kinds=kinds, async_mode=socketio.async_mode)


@main.route('/products')
def products():
    return render_template("category/steinway.html", async_mode=socketio.async_mode)


# 不同品牌商品的商品展示页面
@main.route('/kind/<kind_id>')
def kinds(kind_id):
    products = product.getProductByCategory(kind_id)
    kind = product.getCategoryById(kind_id)
    return render_template("kind_en.html", products=products, kind=kind, async_mode=socketio.async_mode)


@main.route('/kind')
def kinds_edit():
    return render_template("kind-editing.html")


# 商品具体信息页面
@main.route('/productInfo/<product_id>')
def productInfo(product_id):
    commodity = product.getProductById(product_id, record=True)
    # print(product_id)
    # commodity_title = commodity.get('title').get('english')
    return render_template("piano_en.html", commodity=commodity, async_mode=socketio.async_mode)


# 后台页面index
@main.route('/staff_index')
def staff_index():
    return render_template("staff_index.html")


# 后台页面数据展示
@main.route('/backend_data')
def backend_data():
    return render_template("backend_en.html")


# 个人中心展示商品订单
@main.route('/orderList/<user_id>')
@login_required
def userOrderList(user_id):
    orders = user.getOrderByUser(user_id, 0, 100)
    page_size = 5
    if len(orders) % page_size != 0:
        page = len(orders) // page_size + 1
    else:
        page = len(orders) // page_size

    current_page = request.args.get('page', 1, type=int)
    next_page = current_page + 1
    pre_page = current_page - 1
    pre_pos = current_page // 5 * 5 - 1
    next_post = current_page // 5 * 5 + 5
    has_next = True
    has_pre = True
    page_orders = user.getOrderByUser(user_id, (current_page - 1) * page_size, page_size)
    if current_page >= page:
        next_page = None
        has_next = False
    if current_page == 1:
        pre_page = None
        has_pre = False
    pagination = {
        "page": page,
        "current_page": current_page,
        "next_page": next_page,
        "pre_page": pre_page,
        "pre_post": pre_pos,
        "has_next": has_next,
        "has_pre": has_pre,
        "next": next_post
    }
    return render_template("MusiCrashTemplates/orderList.html", user_id=user_id, order_list=page_orders, pagination=pagination)


# 后台展示商品订单
@main.route('/allOrderList')
def allOrderList():
    orders = user.getAllOrder(0, 1000)
    page_size = 5
    if len(orders) % page_size != 0:
        page = len(orders) // page_size + 1
    else:
        page = len(orders) // page_size

    current_page = request.args.get('page', 1, type=int)
    next_page = current_page + 1
    pre_page = current_page - 1
    pre_pos = current_page // 5 * 5 - 1
    next_post = current_page // 5 * 5 + 5
    has_next = True
    has_pre = True
    page_orders = user.getAllOrder((current_page-1)*page_size, page_size)
    if current_page >= page:
        next_page = None
        has_next = False
    if current_page == 1:
        pre_page = None
        has_pre = False
    pagination = {
        "page": page,
        "current_page": current_page,
        "next_page": next_page,
        "pre_page": pre_page,
        "has_next": has_next,
        "has_pre": has_pre,
        "pre_post": pre_pos,
        "next": next_post
    }

    return render_template("orderList_merchant.html", order_list=page_orders, pagination=pagination)


# 后台页面显示商品列表
@main.route('/productList')
def productList():
    products = product.getAllProduct()
    lst = []
    for i in products:
        print(i.id)
        print(1)
        lst += [[product.getCategoryByProduct(i.id), i]]

    return render_template("staff_chat.html", lst=lst)


# 顾客聊天页面弹窗
@main.route('/communicate/1')
@login_required
def communicate():
    return render_template("test_communication_A.html")


@main.route('/conversation/<conversation_id>')
def conversation(conversation_id):
    return render_template("test_communication_A.html", conversation_id=conversation_id)


#订单填写页面
@main.route('/fillBillInfo/<product_id>')
@login_required
def fillBillInfo(product_id):
    piano = product.getProductById(product_id)
    labels = product.getAllCategory()
    return render_template("MusiCrashTemplates/orderForm.html", piano=piano, labels=labels)


@main.route('/about_us')
def aboutus():
    return render_template("MusiCrashTemplates/about_us.html")



@main.route('/checkPhone', methods=['GET', 'POST'])
def check_id():
    phone = request.args.get('phone')
    # user = User.query.filter(User.stu_wor_id == id).all()
    if True:
        return jsonify(code=400, msg="The Phone number has already existed")
    else:
        return jsonify(code=200, msg="this id number is available")

@main.route('/checkEmail', methods=['GET', 'POST'])
def check_email():
    phone = request.args.get('email')
    # user = User.query.filter(User.stu_wor_id == id).all()
    if True:
        return jsonify(code=400, msg="The Email has already existed")
    else:
        return jsonify(code=200, msg="this id number is available")

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



# @main.route('/testio')
# def testio():
#     return render_template("test_io.html", async_mode=socketio.async_mode)
#
#
# @main.route('/testlogin')
# def testlogin():
#     return render_template("test_login.html", async_mode=socketio.async_mode)
#
#
# @main.route('/testorder')
# def testorder():
#     products = product.getAllProduct(0, 50)
#     return render_template("test_order.html", products=products, async_mode=socketio.async_mode)
#
#
# @main.route('/testfuwenben')
# def testfuwenben():
#     return render_template("MusiCrashTemplates/fuwenben.html")
#
#
# @main.route('/testCollection')
# def testCollection():
#     return render_template("MusiCrashTemplates/collectionLists.html")
#
#
# @main.route('/testCommunication')
# def testCommunication():
#     return render_template("test_communication.html")
#
#
# @main.route('/testmodifypw')
# def testmodifypw():
#     return render_template("MusiCrashTemplates/re.html", async_mode=socketio.async_mode)
#
#
# @main.route('/test')
# def test():
#     return render_template("MusiCrashTemplates/test.html", async_mode=socketio.async_mode)
