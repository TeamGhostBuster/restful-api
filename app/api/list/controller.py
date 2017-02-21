from app.util import MongoUtil, JsonUtil
from app.util.AuthUtil import *


@app.route('/user/list/<string:list_id>', methods=['GET'])
@authorized_required
def get_articles_from_list(user, list_id):
    """
    @api {get} /user/list/:id Get articles of a list
    @apiName Get articles of a list
    @apiGroup List

    @apiUse AuthorizationTokenHeader

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

    @apiUse UnauthorizedAccessError
    """
    reading_list = MongoUtil.find_list(list_id)
    # check for bad list
    if reading_list is None:
        return jsonify(msg='List does not exist'), 404

    # convert the articles into json format
    return jsonify(JsonUtil.serialize(reading_list)), 200


@app.route('/user/list', methods=['POST'])
@authorized_required
def create_list(user):
    """
    @api {get} /user/list Create a reading list
    @apiName Create a reading list
    @apiGroup List

    @apiUse AuthorizationTokenHeader

    @apiParam {String} name List name.
    @apiParamExample {json} Request (Example)
        {
            "name": "CMPUT495 Seminar"
        }

    @apiUse UnauthorizedAccessError
    """
    # Get list name from api parameter
    req = request.get_json()
    list_name = req['name']

    # If missing parameter
    if list_name is None:
        return 'Bad request', 400

    # Create a new list
    new_list = MongoUtil.create_list(list_name, user)

    app.logger.info('User {} Create list'.format(user, new_list))

    return jsonify(JsonUtil.serialize(new_list)), 200


@app.route('/user/lists', methods=['GET'])
@authorized_required
def get_user_reading_lists(user):
    """
    @api {get} /user/lists Get user all reading lists
    @apiName Get user reading lists
    @apiGroup List

    @apiUse AuthorizationTokenHeader

    @apiSuccess {String} id User id
    @apiSuccess {Object[]} lists Lists data
    @apiSuccess {String} lists.id List id
    @apiSuccess {String} lists.name List name
    @apiSuccessExample {json} Response (Example):
        {
            "id": "31ladsjfl",
            "lists": [
                {
                    "id": "adlfajdls",
                    "name": "Process"
                }
            ]
        }

    @apiUse UnauthorizedAccessError
    """

    app.logger.info('User: {} Access: [{}]'.format(user, request.full_path))
    return jsonify(JsonUtil.serialize(user)), 200