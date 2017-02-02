from flask import Flask

CONFIG_MAP = {
    'dev': 'config.DevConfig'
}

app = Flask(__name__)
app.config.from_object(CONFIG_MAP['dev'])
app.secret_key='xxxxx'

from app import api
