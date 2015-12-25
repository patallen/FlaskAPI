from app import db
from app import bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    signup_date = db.Column(db.DateTime(), default=db.func.now())
    last_login = db.Column(db.DateTime(), default=db.func.now())

    _password_hash = db.Column(db.String())

    @property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, password):
        self._password_hash = bcrypt.generate_password_hash(password)

    def verify_password(self, password_hash):
        return bcrypt.check_password_hash(self.password, password_hash)
