from flask import request
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature

jss = TimedJSONWebSignatureSerializer('dude')


def get_jwt_payload():
    token_str = request.headers['Authentication']
    try:
        token = token_str.split(' ')[1]
        payload = jss.loads(token)
    except BadSignature:
        return None
    return payload


def create_jwt_token(exp_min, user):
    user = user.username
    token = jss.dumps({
        'username': user
    })
    return token
