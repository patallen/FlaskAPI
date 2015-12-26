from app import app
from models.users import User
from itsdangerous import JSONWebSignatureSerializer
from flask import request, Response

jss = JSONWebSignatureSerializer('dude')


@app.route('/authenticate/', methods=['POST'])
def authenticate_for_jwt():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        try:
            user = User.query.filter_by(username=username).one()
        except:
            user = None

    if user and user.verify_password(password):
        token = jss.dumps({'username': username})
        return Response(token, 200)
    return "NOPE"
