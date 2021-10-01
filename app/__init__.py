from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)
CORS(app, support_credentials=True)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass@127.0.0.1:3306/jobProject'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b4937878ebe4b6:0080f4bb@us-cdbr-east-04.cleardb.com/heroku_41292c346ecbd3a'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app) 

app.config['SECRET_KEY'] = 'test'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)
