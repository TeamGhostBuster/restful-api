from flask import Flask, redirect, url_for, session, request, jsonify
from flask.ext.restplus import Api
from flask_oauthlib.client import OAuth
from app.api.user import User
from app.api.auth import Auth
from config import *

# init
app = Flask(__name__)
app.config.from_object(DevConfig)
app.secret_key = 'development'
api = Api(app)
oauth = OAuth(app)

# google oauth2
google = oauth.remote_app(
    'google',
    consumer_key=app.config.get('CLIENT_ID'),
    consumer_secret=app.config.get('CLIENT_SECRET'),
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


@app.route('/')
def index():
    if 'google_token' in session:
        me = google.get('userinfo')
        return jsonify({"data": me.data})
    return redirect(url_for('login'))


@app.route('/auth/google')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))


@app.route('/auth/google/callback')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    return jsonify({"data": me.data})


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


api.add_resource(User, '/user')
api.add_resource(Auth, '/auth')
