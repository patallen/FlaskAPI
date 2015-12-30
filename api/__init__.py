from app import app
from models.users import User
from flask import request, Response
from decorators import crossdomain, handle_jwt_auth
import json
from .helpers import get_jwt_payload, create_jwt_token


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
        token = create_jwt_token(None, user)
        return Response(token, 200)
    return Response("Could not authenticate user.", 400)


@app.route('/protected/', methods=['POST'])
@handle_jwt_auth
def test_protected():
    """
    This view should only return json if the user is authorized
    via JWT token in header of request.
    This should be completed using a decorator function.
    """
    return Response("You're logged in.", 200)


@app.route('/test/', methods=['POST'])
def test_jwt():
    payload = get_jwt_payload()
    if payload is None:
        return Response("Trouble Authenticating", 400)
    return Response(json.dumps(payload), 200)
