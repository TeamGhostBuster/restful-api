import json
import os
from functools import wraps

import requests

headers = {'Access-Token': 'michaellam.lzc',
           'Provider-Name': 'Google',
           'Content-Type': 'application/json'}

base_url = os.getenv('API_URL', 'http://localhost:5000')

# Global variable that store the ID of document for the sake of time
global global_id
global_id = dict()


def get(url):
    """
    Decorator method to send HTTP GET request
    :param url: The url path
    :return: The response
    """

    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            result = requests.get(base_url + url, headers=headers)
            # return f(result, **kwargs)
            return f(result, **kwargs)

        return wrapped

    return wrapper


def post(url, data=None):
    """
    Decorator method to send HTTP POST request
    :param url: The url path
    :param data: Json body
    :return: The response
    """

    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if len(f.__defaults__) == 2:
                sep_url = url.split('{}')
                if len(sep_url) > 1:
                    url_ids = [global_id[i] for i in f.__defaults__[1]]
                    result = requests.post(base_url + url.format(*url_ids),
                                           headers=headers,
                                           json=data)
                else:
                    json_ids = [global_id[i] for i in f.__defaults__[1]]
                    print('upcoming')
                    print(data.format(*json_ids))
                    result = requests.post(base_url + url,
                                           headers=headers,
                                           json=json.loads(data.format(*json_ids)))
            elif len(f.__defaults__) == 3:
                url_ids = [global_id[i] for i in f.__defaults__[1]]
                json_ids = [global_id[i] for i in f.__defaults__[2]]
                # print('upcoming')
                # print(data.format(*json_ids))
                result = requests.post(base_url + url.format(*url_ids),
                                       headers=headers,
                                       json=json.loads(data.format(*json_ids))[0])
            else:
                result = requests.post(base_url + url,
                                       headers=headers,
                                       json=data)
            return f(result, **kwargs)

        return wrapped

    return wrapper


def delete(url, data=None):
    """
    Decorator method to send HTTP DELETE request
    :param url: The url path
    :param data: The JSON body
    :return: The response
    """

    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if len(f.__defaults__) == 2:
                sep_url = url.split('{}')
                if len(sep_url) > 1:
                    url_ids = [global_id[i] for i in f.__defaults__[1]]
                    result = requests.delete(base_url + url.format(*url_ids),
                                             headers=headers,
                                             json=data)
                else:
                    json_ids = [global_id[i] for i in f.__defaults__[1]]
                    result = requests.delete(base_url + url,
                                             headers=headers,
                                             json=json.loads(data.format(*json_ids))[0])
            elif len(f.__defaults__) == 3:
                url_ids = [global_id[i] for i in f.__defaults__[1]]
                json_ids = [global_id[i] for i in f.__defaults__[2]]
                result = requests.delete(base_url + url.format(*url_ids),
                                         headers=headers,
                                         json=json.loads(data.format(*json_ids))[0])
            else:
                result = requests.delete(base_url + url,
                                         headers=headers,
                                         json=data)
            return f(result, **kwargs)

        return wrapped

    return wrapper


def put(url, data=None):
    """
    Decorator method to send HTTP PUT request
    :param url: The url path
    :param data: The JSON body
    :return: The response
    """

    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if len(f.__defaults__) == 2:
                sep_url = url.split('{}')
                if len(sep_url) > 1:
                    url_ids = [global_id[i] for i in f.__defaults__[1]]
                    result = requests.put(base_url + url.format(*url_ids),
                                          headers=headers,
                                          json=data)
                else:
                    json_ids = [global_id[i] for i in f.__defaults__[1]]
                    result = requests.put(base_url + url,
                                          headers=headers,
                                          json=json.loads(data.format(*json_ids))[0])
            elif len(f.__defaults__) == 3:
                url_ids = [global_id[i] for i in f.__defaults__[1]]
                json_ids = [global_id[i] for i in f.__defaults__[2]]
                result = requests.put(base_url + url.format(*url_ids),
                                      headers=headers,
                                      json=json.loads(data.format(*json_ids))[0])
            else:
                result = requests.put(base_url + url,
                                      headers=headers,
                                      json=data)
            return f(result, **kwargs)

        return wrapped

    return wrapper
