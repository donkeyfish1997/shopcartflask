from app import app
from flask_cors import cross_origin
from app.view import user
from app.view import productView


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

@app.route("/user/orderList", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def orderList():
    return productView.orderList()
@app.route("/user/cartList", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def cartList():
    return productView.cartList()
@app.route("/user/cartDel", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def cartDel():
    return productView.cartDel()


@app.route("/user/getUsernameFromSession", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def getUsernameFromSession():
    return user.getUsernameFromSession()

@app.route("/user/avatar/<username>")
def getAvatar(username):
    return user.getAvatar(username)

@app.route("/search")
@cross_origin(supports_credentials=True)
def search():
    return productView.search()


@app.route("/product")
@cross_origin(supports_credentials=True)
def product():
    return productView.product()

@app.route("/product/addOrder",methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def addOrder():
    return productView.addOrder()

@app.route("/product/addCart",methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def addCart():
    return productView.addCart()

if __name__ == "__main__":
    app.run()

