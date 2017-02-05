from flask import request
from app.config import *
from app.api.user.model import User
import httplib2
import json


def get_auth_info():
    # access_token = request.headers['Access-Token']
    access_token = 'ya29.GlzpAy7pIMrPYhNACY7CQRyGw7PEerLFcXAuKC2Fz1NodEXC3YLdMoeNyMsTEDd12oWriEPNdSnhiiP7TYsfFLwB1EZzNq25Jby107vjyTOsBwd4sgcjDih-v53qpg'
    if access_token is not None:
        # Check that the Access Token is valid.
        url = ('https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=%s'
               % access_token)
        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1].decode('utf-8'))
        if result.get('error') is not None:
            return None
        # elif result['issued_to'] != BaseConfig.CONFIG['google']['client_key']:
        #     return None
        print(result)
        print(result['email'])
    user = User.objects(email_exact=result['email'])
    print('hello')
    if user is None:
        print("no")
