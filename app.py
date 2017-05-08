from flask import Flask, request, session, redirect, render_template
from flask import url_for
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_restful import abort

from util import CommonUtil

app = Flask(__name__)
app.config.update(
    # MONGO_URI='mongodb://172.27.12.67:27017/sun',
    MONGO_URI='mongodb://localhost:27017/sun',
    MONGO_CURSORCLASS='DictCursor',
)
app.config['SECRET_KEY'] = '<the super secret key comes here>'

logger = CommonUtil.logger
login_manager = LoginManager()
login_manager.init_app(app)

mongo = PyMongo(app)


# session['username'] = 'admin'


@app.route('/index')
def index():
    return "Hello Flask"


@app.route('/add_user', methods=['POST'])
def add_user():
    # user = {'name': 'Michael', 'age': 18, 'scores': [{'course': 'Math', 'score': 76}]}
    post_data = request.get_json()
    logger.info(post_data)
    if post_data['username'] == '' or post_data['password'] == '':
        abort(400)
    # if User.query.filter_by(username=username).first() is not None:
    #     abort(400)  # existing user
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


@app.route('/return_login', methods=['GET'])
def return_login():
    return render_template('login.html')


def query_user(filter_doc):
    user_cursor = mongo.db['users'].find(filter_doc)
    user_list = [user for user in user_cursor]
    logger.info(user_list)
    return user_list


# @app.route('/return_logout')
# def return_logout():
#     return redirect("/logout")


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('return_login'))


@app.route('/')
def index_or_login():
    if 'username' in session:
        return redirect('/index')
    return redirect('/return_login')


if __name__ == '__main__':
    app = app.run(port=2333, debug=True)
