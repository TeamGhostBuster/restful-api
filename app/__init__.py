import os

from flask import Flask
from flask_mongoengine import MongoEngine

config = {
    'prod': 'app.config.ProductionConfig',
    'deploy': 'app.config.DeployConfig',
    'dev': 'app.config.DevelopmentConfig'
}

# initialize flask instance
app = Flask(__name__)
app.config['MONGODB_DB'] = 'raspberry'

# initialize MongoEngine instance
db = MongoEngine(app)

# read environment variable from the system
config_name = os.getenv('FLASK_CONFIGURATION')
app.config.from_object(config[config_name])

# import api module
from app import api
