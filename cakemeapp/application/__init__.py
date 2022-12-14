# import Flask class from the flask module
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv


# create a new instance of Flask and store it in app
app = Flask(__name__)

if sys.platform == 'darwin':
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/cakeme"
else:
   app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/cakeme"

# app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST') + '/' + getenv('MYSQL_DB'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


# link our app to the persistence layer
db = SQLAlchemy(app)