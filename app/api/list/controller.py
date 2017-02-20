from app import app
from app.util.AuthUtil import *
from app.util import MongoUtil
from bson.objectid import ObjectId


@app.route('/user/list/<string:list_id>', methods=['GET'])
@authorized_required
def get_articles_from_list(user, list_id):
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
            "articles": [
                {
                    "id": "adlfajdls",
                    "title": "Process"
                }
            ]
        }
    """
    # check for bad list
    if list_id is None:
        return 'Bad request', 400

    reading_list = List.objects.get(id=ObjectId(list_id))

    # convert the articles into json format
    
    return jsonify(id=reading_list.id, name=reading_list.name, articles=reading_list.articles)


@app.route('/user/list', methods=['POST'])
@authorized_required
def create_list(user):
    """
    @api {get} /user/list Create a reading list
    @apiName Create a reading list
    @apiGroup List

    @apiHeader {String} Access-Token Access token obtains from Oauth2 provider.
    @apiHeader {String} Provider-Name Oauth2 provider name.
    @apiHeaderExample {json} Header (Example):
        {
            "Access-Token": "12xsdklajlkadsf",
            "Provider-Name": "Google"
        }

    @apiParam {String} name List name.
    """
    # Get list name from api parameter
    req = request.get_json()
    list_name = req['name']

    # If missing parameter
    if list_name is None:
        return 'Bad request', 400

    # Create a new list
    MongoUtil.create_list(list_name, user)
    return jsonify(msg='success'), 200
