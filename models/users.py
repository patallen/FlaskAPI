from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    signup_date = db.Column(db.DateTime(), default=db.func.now())
    last_login = db.Column(db.DateTime(), default=db.func.now())
