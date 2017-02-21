from app.util import JsonUtil
from app.util import MongoUtil
from app.util.AuthUtil import *


@app.route('/user/article/<string:article_id>', methods=['GET'])
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
            "description": "adlsfjdlask",
            "url": "https://www.google.com/something",
            "list_id": "ladsjflas",
            "comments" : [{
                "id": "afjlkdsfjafla",
                "content": "i hate it",
                "timestamp": "2017-02-04-19-59-59"
            }],
            "tags": ["science", "computer"]
        }

    @apiUse UnauthorizedAccessError
    """
    article = MongoUtil.find_article(article_id)

    if article is None:
        return jsonify(msg='Articles does not exist'), 404

    return jsonify(JsonUtil.serialize(article)), 200


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
            "description": "I don't know",
            "url": "https://www.gooel.com/something",
            "tags": ["tag1", "tag2", "tag3"]
        }

    @apiSuccess {String} Message Success message.

    @apiUse UnauthorizedAccessError
    @apiUse ListDoesNotExist
    """
    # Parse request
    req = request.get_json()
    title = req.get('title')
    list_id = req.get('list_id')
    description = req.get('description')
    url = req.get('url')
    tags = req.get('tags')

    # Validate request
    if not 'title' or not 'list_id':
        return jsonify({
            'msg': 'Invalid request'
        }), 400

    # Create article
    new_article = MongoUtil.create_article(title, list_id, description, url, tags)

    if new_article is None:
        return jsonify({
            'msg': 'List does not exist'
        }), 400

    app.logger.info('User {} Create article {}'.format(user, new_article))
    return jsonify({'msg': 'Success'}), 200


@app.route('/user/article/<string:article_id>/tag')
@authorized_required
def add_tags(user, article_id):
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
            "tag": "science"
        }

    @apiSuccess {String} Message Success message.

    @apiUse UnauthorizedAccessError
    @apiUse ListDoesNotExist
    """
    req = request.get_json()
    tag = req.get('tag')
    article = MongoUtil.add_tag(article_id, tag)

    if article is None:
        return jsonify({
            'msg': 'List does not exist'
        }), 400

    app.logger.info('User {} Add tag {} to {}'.format(user, tag, article))

    return jsonify(msg='Success'), 200
