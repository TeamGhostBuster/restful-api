import requests

from flask import request
from bson.objectid import ObjectId, InvalidId

from app import app
from app.config import *
from app.util import MongoUtil


def get_auth_info():
    """
    Get user's identity

    Verify the interity of token from the OAuth provider,
    then look up the database check if user exist or not.
    If the user does not exist, create a new user instead.

    :return: user instance
    """
    if 'Access-Token' not in request.headers:
        return None

    access_token = request.headers['Access-Token']
    if access_token is not None:
        # For development purpose only
        if access_token in app.config['TEST_TOKEN'].keys():
            user = MongoUtil.find_user(app.config['TEST_TOKEN'][access_token])
        else:
            # Check that the Access Token is valid.
            url = ('https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=%s'
                   % access_token)
            result = requests.get(url).json()
            if result.get('error_description') is not None:
                return None

            user = MongoUtil.find_user(result['email'])

    if user is None:
        # if user does not exist, create a new user instead
        app.logger.info('Create User: {}'.format(user))
        first_name, last_name = get_user_profile(access_token)
        user = MongoUtil.create_user(result['email'], first_name, last_name)

    return user


def get_user_profile(access_token):
    url = 'https://www.googleapis.com/plus/v1/people/me?access_token={}'.format(access_token)
    result = requests.get(url).json()
    if result.get('error') is not None:
        return None
    return result['name']['givenName'], result['name']['familyName']


def validate_id(objectid):
    """
    Validate the incoming objectid of item
    :param objectid: The id in string
    :return: True/False
    """
    try:
        ObjectId(objectid)
    except InvalidId:
        return False

    return True


def check_group_read_permission(user):
    # Parse request
    req = get_request()

    if req is None:
        return None

    group_id = req.get('group_id', None)

    if group_id is None:
        return None

    if MongoUtil.check_user_in_group(user, group_id) is None:
        return None

    return user


def get_request():
    """
    Parse request, convert empty string or 'null' into None type in python
    :return:
    """
    if request.get_json() is not None:
        return {k: v if v != '' and v != 'null' else None for k, v in request.get_json().items()}
