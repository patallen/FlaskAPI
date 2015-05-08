from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Api
from datetime import datetime
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///polls.db'
api = Api(app)
db = SQLAlchemy(app)

class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(200), nullable=False)
	pub_date = db.Column(db.Date)
	choices = db.relationship('Choice')

	def __init__(self, text):
		self.text = text
		self.pub_date = datetime.utcnow()


class Choice(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(240), nullable=False)
	votes = db.Column(db.Integer, default=0)
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

	def __init__(self, question_id, text):
		self.text = text
		self.question_id = question_id


class Poll(Resource):
    def get(self, poll_id):
		question = Question.query.filter_by(id=poll_id).one()
		choices = question.choices
		return {'question': question.text}

api.add_resource(Poll, '/poll/<int:poll_id>')