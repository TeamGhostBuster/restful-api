from app import app
from app.util.AuthUtil import *


@app.route('/user/list/:id', methods=['GET'])
@authorized_required
def get_articles_from_list(list_id):
    """
    @api {get} /user/list/:id Get articles of a list
    @apiName Get articles of a list
    @apiGroup List

    @apiHeader {String} Access-Token Access token obtains from Oauth2 provider.
    @apiHeader {String} Provider-Name Oauth2 provider name.
    @apiHeaderExample {json} Header (Example):
        {
            "Access-Token": "12xsdklajlkadsf",
            "Provider-Name": "Google"
        }

    @apiParam {String} id List unique ID.

    @apiSuccess {String} List id.
    @apiSuccess {String} List name.
    @apiSuccess {Object[]} articles Articles data.
    @apiSuccess {String} articles.id Article id.
    @apiSuccess {String} article.title Article title.
    @apiSuccessExample {json} Response (Example):
        {
            "id": "31ladsjfl",
            "name": "CMPUT 391 Seminar",
            "articles": [{
                "id": "adlfajdls",
                "title": "Process"
            }]
        }
    """
    return 'success', 200
