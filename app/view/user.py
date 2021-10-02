from flask import jsonify, request, session,Response
import json
from ..model import user


def addUser():
    info = json.loads(request.data)
    status = user._add(**info)
    if not status[0]:
        print(status[1])
        return jsonify(status[1]), 403
    session['username'] = info['username']
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
    resp = user._getAvatar(name)
    return resp
    

