from app import app


@app.route('/user/article/:id', methods=['GET'])
def get_article(article_id):
    """
    @api {get} /user/article/:id Get a article
    @apiName Get a article
    @apiGroup Article

    @apiHeader {String} Access-Token Access token obtains from Oauth2 provider.
    @apiHeader {String} Provider-Name Oauth2 provider name.
    @apiHeaderExample {json} Header (Example):
        {
            "Access-Token": "12xsdklajlkadsf",
            "Provider-Name": "Google"
        }

    @apiParam {String} id Article unique ID.

    @apiSuccess {String} id Article id.
    @apiSuccess {String} title Article title.
    @apiSuccess {String} list_id List id.
    @apiSuccess {Object[]} comments User comments.
    @apiSuccess {Object} comments.content The content.
    @apiSuccess {String} comments.timestamp The timestamp of the comment.
    @apiSuccessExample {json} Response (Example):
        {
            "id": "aldkfjadls",
            "title": "Process",
            "list_id": "ladsjflas",
            "comments" : [{
                "content": "i hate it",
                "timestamp": "2017-02-04-19-59-59"
            }]
        }
    """
    pass

# TODO more resources for articles
