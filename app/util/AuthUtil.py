from functools import wraps

from flask import jsonify

from .RequestUtil import *


def authorized_required(f):
    """
    Decorated function that check if user is logged in

    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if get_auth_info() is None:
            return jsonify({'msg': 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated_function

