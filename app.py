from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///polls.db'
api = Api(app)
db = SQLAlchemy(app)
