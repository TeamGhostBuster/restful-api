class BaseConfig(object):
    DEBUG = False

    # MongoDB setting
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017

    # Oauth2 token setting
    SECRET_KEY = 'xxxxx'
    CONFIG = {
        'google': {
            'client_key': '224926533228-4jcfs0862eib0vo9j81b9d6h8agqh30f.apps.googleusercontent.com',
        }
    }


class ProductionConfig(BaseConfig):
    DEBUG = False


class DeployConfig(BaseConfig):
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    CLIENT_URL = 'demo.vfree.org'
    SERVER_NAME = 'api.vfree.org:5000'