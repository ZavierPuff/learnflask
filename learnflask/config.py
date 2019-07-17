from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URL'] = \
    "mysql + pymysql://root:m1024@localhost/myoffice?charset=utf-8"
db = SQLAlchemy(app)