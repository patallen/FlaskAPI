from datetime import timedelta
from itsdangerous import TimedJSONWebSignatureSerializer
from flask import make_response, request, current_app, Response
from functools import update_wrapper, wraps
from .helpers import get_jwt_payload

from app import app

jss = TimedJSONWebSignatureSerializer(app.config['JWT_SECRET'])


def handle_jwt_auth(f):
    """
    View decorator that checks that the JWT token in the request
    is valid. If so, it returns the view's response and updates the header
    with a new JWT token with new exp field.
    """
    @wraps(f)
    def wrapped_function(*args, **kwargs):
        payload = get_jwt_payload()
        if payload is None:
            return Response("PROTECTED - Please sign in.", 400)

        token = jss.dumps(payload)
        resp = make_response(f(*args, **kwargs))
        resp.headers['Authentication'] = "Bearer {}".format(token)
        return resp

    return wrapped_function


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator
