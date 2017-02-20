from app import app
from app.util.AuthUtil import *


@app.route('/user/article/:id', methods=['GET'])
@authorized_required
def get_article(user, article_id):
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
    return 'success', 200


@app.route('/user/article', methods=['POST'])
@authorized_required
def create_article(user):
    """
    @api {post} /user/article/ Create a article
    @apiName Create a article
    @apiGroup Article

    @apiHeader {String} Access-Token Access token obtains from Oauth2 provider.
    @apiHeader {String} Provider-Name Oauth2 provider name.
    @apiHeaderExample {json} Header (Example):
        {
            "Access-Token": "12xsdklajlkadsf",
            "Provider-Name": "Google"
        }

    @apiParam {String} title The article title.
    @apiParam {Json} tags The user custom tags.
    @apiParamExample {json} Request (Example):
        {
            "title": "God know what it is",
            "list_id": "aldkfjdaslkfjl",
            "tags": {
                "key1": "value1",
                "key2": "value2"
            }
        }

    @apiSuccess {String} Message Success message.
    """

    return 'success', 200
