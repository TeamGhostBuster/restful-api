from app import app


@app.route('/auth/<provider_name>', methods=['GET', 'POST'])
def auth(provider_name):
    """
    @api {get} /auth/:provider Authenticate with Oauth2 provider
    @apiName Authentication
    @apiGroup Auth

    @apiParam {provider} Oauth2 provider name.

    """
    return provider_name
