from app import app
from models.users import User
from itsdangerous import JSONWebSignatureSerializer, BadSignature
from flask import request, Response
from decorators import crossdomain
import json


jss = JSONWebSignatureSerializer('dude')


@app.route('/authenticate/', methods=['POST'])
@crossdomain(origin="*")
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
    return Response("Could not authenticate user.", 400)


@app.route('/test/', methods=['POST'])
def test_jwt():
    payload = get_jwt_payload()
    if payload is None:
        return Response("Trouble Authenticating", 400)
    return Response(json.dumps(payload), 200)


def get_jwt_payload():
    token_str = request.headers['Authentication']
    try:
        token = token_str.split(' ')[1]
        payload = jss.loads(token)
    except BadSignature:
        return None
    return payload
