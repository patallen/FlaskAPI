from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
api = Api(app)
db = SQLAlchemy(app)

class TodoTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)


parser = reqparse.RequestParser()
parser.add_argument('task', type=str, required=True)

class Task(Resource):
    def get(self, task_id):
        """Returns a task based on its ID"""
        task = TodoTask.query.one(id=task_id)
        return {'item': 'this is item 1'}

api.add_resource(Todo, '/todos', '/todos/<int:task_id>')
if __name__ == '__main__':
    app.run(debug=True)
