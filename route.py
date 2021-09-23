from app import app
from flask_cors import cross_origin
from app.view import user


@app.route("/")
def index():
    return 'index'


@app.route("/user/add", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def addUser():
    return user.addUser()


@app.route("/user/login", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def login():
    return user.login()


@app.route("/user/logout", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def logout():
    return user.logout()


@app.route("/user/isLogined", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def isLogined():
    return user.isLogined()


@app.route("/user/getUsernameFromSession", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def getUsernameFromSession():
    return user.getUsernameFromSession()


@app.route("/search")
@cross_origin(supports_credentials=True)
def search():
    return user.search()


@app.route("/product")
@cross_origin(supports_credentials=True)
def product():
    return user.product()
