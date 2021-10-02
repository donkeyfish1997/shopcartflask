from app import app,db
from flask_cors import cross_origin,CORS
from app.view import user
from app.view import productView

CORS(app,headers=['Content-Type'],origins=["https://shopcartvue.herokuapp.com"], expose_headers=['Access-Control-Allow-Origin'],  supports_credentials=True)

@app.route("/")
def index():
    return 'index'


@app.route("/user/add", methods=['GET', 'POST'])
def addUser():
    return user.addUser()


@app.route("/user/login", methods=['GET', 'POST'])
def login():
    return user.login()


@app.route("/user/logout", methods=['GET', 'POST'])
def logout():
    return user.logout()


@app.route("/user/isLogined", methods=['GET', 'POST'])
def isLogined():
    return user.isLogined()

@app.route("/user/orderList", methods=['GET', 'POST'])
def orderList():
    return productView.orderList()
@app.route("/user/cartList", methods=['GET', 'POST'])
def cartList():
    return productView.cartList()
@app.route("/user/cartDel", methods=['GET', 'POST'])
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
# @app.route("/createTable")
# def create():
#     db.create_all()
#     db.session.commit()
#     return '123'
app.debug = True
if __name__ == "__main__":
    app.run()
    pass

