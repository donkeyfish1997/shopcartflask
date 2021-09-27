from .. import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    userId = db.Column(db.Integer, nullable=False )
    productId = db.Column(db.String(30), nullable=False)
    pic = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    userId = db.Column(db.Integer, nullable=False )
    productId = db.Column(db.String(30), nullable=False)
    pic = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    def __repr__(self) -> str:
        return f'id:{self.id}userId:{self.userId}productId:{self.productId}pic:{self.pic}name:{self.name}price:{self.price}'

def _addOrder(userId,**args):
    info = Order(userId=userId,**args)
    db.session.add(info)
    db.session.commit()
    return (True,)

def _addCart(userId,**args):
    if Cart.query.filter_by(userId=userId).filter_by(productId=args['productId']).first():
        print('已加入')
        return (True)
    

    info = Cart(userId=userId,**args)
    print('info',info)
    db.session.add(info)
    db.session.commit()
    return (True,)

def _orderList(userId):
    info = Order.query.filter_by(userId=userId).all()
    tmp = []
    for i in info:
        tmp.append({'Id':i.productId,'picB':i.pic,'name':i.name,'price':i.price,})
    return tmp
def _cartList(userId):
    info = Cart.query.filter_by(userId=userId).all()
    tmp = []
    for i in info:
        tmp.append({'Id':i.productId,'picB':i.pic,'name':i.name,'price':i.price,})
    return tmp

def _cartDel(userId,productId):
    product = Cart.query.filter_by(userId=userId).filter_by(productId=productId).first()
    db.session.delete(product)
    db.session.commit()
    return True


