from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///polls.db'
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from api import *
