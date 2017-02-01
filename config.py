import os
basedir = os.path.abspath(os.path.dirname(__file__))


CONFIG = {
    'google': {
        'consumer_key': '224926533228-4jcfs0862eib0vo9j81b9d6h8agqh30f.apps.googleusercontent.com',
        'consumer_secret': '-S83L_MmW8OE4eB8AvuvCxxo',
    }
}


class Config(object):
    DEBUG = False
    CLIENT_ID = '224926533228-4jcfs0862eib0vo9j81b9d6h8agqh30f.apps.googleusercontent.com'
    CLIENT_SECRET = '-S83L_MmW8OE4eB8AvuvCxxo'
    port = 5000

class DevConfig(Config):
    DEBUG = True
