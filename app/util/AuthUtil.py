from functools import wraps

from flask import jsonify

from .RequestUtil import *


def authorized_required(f):
    """
    Decorated function that check if user's token is valid

    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = get_auth_info()
        if get_auth_info() is None:
            return jsonify({'msg': 'Unauthorized access'}), 401
        return f(user, **kwargs)
    return decorated_function

