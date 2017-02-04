from app import app


@app.route('/user/library', methods=['GET'])
def get_user_reading_lists():
    """
    @api {get} /user/library Get user reading lists
    @apiName Get user reading lists
    @apiGroup Library

    @apiHeader {String} Access-Token Access token obtains from Oauth2 provider.
    @apiHeader {String} Provider-Name Oauth2 provider name.
    @apiHeaderExample {json} Header (Example):
        {
            "Access-Token": "12xsdklajlkadsf",
            "Provider-Name": "Google"
        }

    @apiSuccess {String} id User id
    @apiSuccess {Object[]} lists Lists data
    @apiSuccess {String} lists.id List id
    @apiSuccess {String} lists.name List name
    @apiSuccessExample {json} Response (Example):
        {
            "id": "31ladsjfl",
            "lists": [{
                "id": "adlfajdls",
                "name": "Process"
            }]
        }
    """
    pass
