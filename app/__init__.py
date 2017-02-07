import os
from logging import Formatter
from logging.handlers import RotatingFileHandler

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

file_handler = RotatingFileHandler('info.log', maxBytes=10000, backupCount=1)
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
))
app.logger.addHandler(file_handler)

# import api module
from app import api
