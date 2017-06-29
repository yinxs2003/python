# coding=utf-8
from flask import Flask, request, session, redirect, render_template
from flask import url_for
from flask_flatpages import FlatPages
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_restful import abort

from util import CommonUtil

app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb://admin:admin@172.27.12.67:27017/sun',
    # MONGO_URI='mongodb://localhost:27017/sun',
    MONGO_CURSORCLASS='DictCursor',
)
app.config['SECRET_KEY'] = '<the super secret key comes here>'
flatpages = FlatPages(app)

logger = CommonUtil.logger
login_manager = LoginManager()
login_manager.init_app(app)

mongo = PyMongo(app)


def checkLogin(func):
    # 返回一个注解类
    from functools import wraps
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not session.has_key('username') or session['username'] == 0:
            # redirect = {"status": 302, "location": '/login.html'}
            return render_template('login.html')
        return func(*args, **kwargs)

    return decorated_function


@app.route('/')
# @checkLogin
def index():
    pages = (p for p in flatpages if 'date' in p.meta)
    return render_template('index.html', pages=pages)


@app.route('/pages/<path:path>/')
def page(path):
    return render_template('page.html', page=flatpages.get_or_404(path))


@app.route('/add_user', methods=['POST'])
# @checkLogin
def add_user():
    post_data = request.get_json()
    logger.info(post_data)
    if post_data['username'] == '' or post_data['password'] == '':
        abort(400)
    try:
        mongo.db['users'].insert_one(post_data)
        return "Inserted Successfully!"
    except Exception as e:
        logger.error(e)
        return "Inserted Failed"


@app.route('/login', methods=['POST'])
def login():
    request_user = {}
    username = request.form['username']
    password = request.form['password']

    if username == '' or password == '':
        abort(400)

    request_user.setdefault("username", username)
    user_in_db = query_user(request_user)
    if user_in_db and user_in_db[0]['password'] == password:
        session['username'] = username
        return render_template("index.html")
    return "not a register"


def query_user(filter_doc):
    user_cursor = mongo.db['users'].find(filter_doc)
    user_list = [user for user in user_cursor]
    logger.info(user_list)
    return user_list


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('return_login'))


if __name__ == '__main__':
    app = app.run(port=2333, debug=True)
