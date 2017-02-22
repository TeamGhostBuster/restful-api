class BaseConfig(object):
    DEBUG = False

    MONGODB_SETTINGS = {
        'DB': 'raspberry',
        'HOST': '127.0.0.1',
        'PORT': 27017
    }

    # Oauth2 token setting
    SECRET_KEY = 'xxxxx'
    CONFIG = {
        'google': {
            'client_key': '224926533228-4jcfs0862eib0vo9j81b9d6h8agqh30f.apps.googleusercontent.com',
        }
    }

    # Access token for testing
    TEST_TOKEN = {
        'michaellam.lzc': 'michaellam.lzc@gmail.com',
        'zichun3': 'zichun3@ualberta.ca',
        'sdlarsen': 'sdlarsen@ualberta.ca'
    }


class ProductionConfig(BaseConfig):
    DEBUG = False


class DeployConfig(BaseConfig):
    DEBUG = True

    MONGODB_SETTINGS = {
        'DB': 'raspberry',
        'HOST': 'mongo',
        'PORT': 27017
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = True
