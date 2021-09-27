from flask import jsonify, request, session
import json
from ..lib.pchome import pchomeSearch,pchomeitem
from ..model import productModel
def search():
    keyword = request.args.get('keyword')
    page = request.args.get('page')
    data = pchomeSearch(keyword,page)
    return jsonify(data)

def product():
    id = request.args.get('id')
    data = pchomeitem(id)
    return jsonify(data)

def addOrder():
    id = session.get('id')
    info = json.loads(request.data)
    productModel._addOrder(id,**info)
    return 'ok'

def addCart():
    id = session.get('id')
    info = json.loads(request.data)
    productModel._addCart(id,**info)
    return 'ok'

def orderList():
    id = session.get('id')
    return jsonify(productModel._orderList(id))

def cartList():
    id = session.get('id')
    return jsonify(productModel._cartList(id))


def cartDel():
    id = session.get('id')
    productId = request.args['id']
    productModel._cartDel(id,productId)
    return '已刪除'