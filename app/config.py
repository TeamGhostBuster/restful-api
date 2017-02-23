from pymongo.read_preferences import ReadPreference


class BaseConfig(object):
    DEBUG = False

    MONGODB_SETTINGS = {
        'DB': 'raspberry',
        'HOST': '127.0.0.1',
        'PORT': 27017
    }

    ELASTICSEARCH_SETTINGS = {
        'ELASTICSEARCH_HOST': ['localhost'],
        'ELASTICSEARCH_AUTH': ('elastic', 'changeme'),
        'ELASTICSEARCH_PORT': 9200
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
        'HOST': 'mongodb://mongo,mongo1,mongo2/raspberry',
        'PORT': 27017,
        'replicaset': 'mongo-replica',
        'READ_PREFERENCE': ReadPreference.SECONDARY
    }

    ELASTICSEARCH_SETTINGS = {
        'ELASTICSEARCH_HOST': 'elasticsearch',
        'ELASTICSEARCH_AUTH': ('elastic', 'changeme'),
        'ELASTICSEARCH_PORT': 9200
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = True
