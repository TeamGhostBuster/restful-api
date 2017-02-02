from app import app
from flask_oauthlib.client import OAuth
from flask import session, url_for, redirect, jsonify, request

# hardcoded for now
# for testing purposes

oauth = OAuth(app)

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
    return redirect(url_for('auth', provider_name='google'))


@app.route('/auth/<provider_name>', methods=['GET', 'POST'])
def auth(provider_name):
    """
    @api {get} /auth/:provider Authenticate with Oauth2 provider
    @apiName Authentication
    @apiGroup Auth

    @apiParam {provider} Oauth2 provider name.
    """
    return google.authorize(callback=url_for('authorized', provider_name=provider_name, _external=True))


@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))


@app.route('/auth/<provider_name>/authorized')
def authorized(provider_name):
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
