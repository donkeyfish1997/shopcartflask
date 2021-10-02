from .. import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    pic=db.Column(db.TEXT)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    sex = db.Column(db.String(5), nullable=False)
    text = db.Column(db.String(30))

    def __repr__(self):
        return f'username:{self.username}, email:{self.email}, password:{self.password}, sex:{self.sex}, text:{self.text},'


def _add(**args):
    print(args)
    if User.query.filter_by(username=args['username']).first():
        return (False,{'username':'username 已被使用過'})
    if User.query.filter_by(email=args['email']).first():

        return (False,{'email':'email 已被使用過'})
    info = User(**args)
    db.session.add(info)
    db.session.commit()
    return (True,)

def _login(**args):
    user = User.query.filter_by(email=args['email'],password = args['password']).first()
    if user:
        return user
    return None
def _getAvatar(name):
    user = User.query.filter_by(username=name).first()
    if user:
        return user.pic
    return None