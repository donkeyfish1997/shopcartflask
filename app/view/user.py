from flask import jsonify, request, session,Response
import json
from ..model import user
from binascii import a2b_base64
from ..lib.Avatar import seavAvatar
import pickle

def addUser():
    info = json.loads(request.data)
    pic = info.pop('pic')
    status = user._add(**info)
    if not status[0]:
        print(status[1])
        return jsonify(status[1]), 403
    session['username'] = info['username']
    if pic:
        seavAvatar(pic,info['username'])
    return jsonify('成功'), 200


def login():
    info = json.loads(request.data)

    loginInfo = user._login(**info)
    if loginInfo:
        print('username', loginInfo)
        session['username'] = loginInfo.username
        session['id'] = loginInfo.id
        return 'susses'
        # return jsonify('成功'), 200
    return jsonify(err='信箱或密碼不符'), 403


def logout():
    session.clear()
    return 'logout!'


def getUsernameFromSession():
    username = session.get('username')
    print(username)
    if username:
        return jsonify(username), 200
    return '並沒有登入', 403

def getAvatar(name):
    try:
        with open(f"pic/avatar/{name}.png", 'rb') as f:
            image = f.read()
        resp = Response(image, mimetype="image/jpeg")
        return resp
    except:
        with open("pic/noAva.png", 'rb') as f:
            image = f.read()
        resp = Response(image, mimetype="image/jpeg")
        return resp
    

