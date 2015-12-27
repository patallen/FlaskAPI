from app import app
from models.users import User
from itsdangerous import JSONWebSignatureSerializer
from flask import request, Response
from decorators import crossdomain

import pprint

jss = JSONWebSignatureSerializer('dude')


@app.route('/authenticate/', methods=['POST'])
@crossdomain(origin="*")
def authenticate_for_jwt():
    pprint.pprint(request.headers)
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
    return Response("Could not authenticate user.", 400)
