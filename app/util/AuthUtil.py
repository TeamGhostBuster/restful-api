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


def group_read_permission_required(f):
    """
    Check if user has permission to access the group info
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = check_group_read_permission(get_auth_info())
        if user is None:
            return jsonify({'msg': 'User does not have group read permission'}), 401
        return f(user, **kwargs)

    return decorated_function
