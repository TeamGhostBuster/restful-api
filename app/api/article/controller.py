from app.util import ElasticSearchUtil
from app.util import JsonUtil, RequestUtil, ResponseUtil
from app.util.AuthUtil import *
import os


@app.route('/user/article/<string:article_id>', methods=['GET'])
@authorized_required
def get_article(user, article_id):
    """
    @api {get} /user/article/:id Get a article in personal list
    @apiName Get a article in personal list
    @apiGroup Article

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id The Article id

    @apiSuccess {String} id Article id.
    @apiSuccess {String} title Article title.
    @apiSuccess {Object[]} comments User comments.
    @apiSuccess {String} comments.id The comment id.
    @apiSuccess {String} comments.content The content.
    @apiSuccess {String} comments.timestamp The timestamp of the comment.
    @apiSuccess {Email} comments.author The author's email.
    @apiSuccessExample {json} Response (Example):
        {
            "id": "aldkfjadls",
            "title": "Process",
            "description": "adlsfjdlask",
            "url": "https://www.google.com/something",
            "comments" : [{
                "id": "afjlkdsfjafla",
                "content": "i hate it",
                "created_at": "2017-02-04-19-59-59",
                "author": "tester@ualberta.ca"
            }],
            "tags": ["science", "computer"]
        }

    @apiUse UnauthorizedAccessError
    """
    # Find article from the database
    article = MongoUtil.find_article(article_id)

    # If the article does not exist
    if article is None:
        return jsonify(msg='Articles does not exist'), 404

    app.logger.info('User {} Get article {}'.format(user, article))
    return jsonify(JsonUtil.serialize(article)), 200


@app.route('/user/list/<string:list_id>/article', methods=['POST'])
@authorized_required
def create_article(user, list_id):
    """
    @api {post} /user/list/:id/article/ Create a article for user
    @apiName Create a article for user
    @apiGroup Article

    @apiUse AuthorizationTokenHeader

    @apiParam {String} list_id The list id.
    @apiParam {String} title The article title.
    @apiParam {String} description The description.
    @apiParam {String} [url] The url to the article.
    @apiParam {Json} [tags] The user custom tags.
    @apiParamExample {json} Request (Example):
        {
            "title": "God know what it is",
            "list_id": "aldkfjdaslkfjl",
            "description": "I don't know",
            "url": "https://www.gooel.com/something",
            "tags": ["tag1", "tag2", "tag3"]
        }

    @apiSuccess {json} Article json representation.
    @apiSuccessExample {json} Respond (Example)
        {
            "id": "adlkfdalfjk",
            "title": "God know what it is",
            "description": "I don't know",
            "url": "https://www.gooel.com/something",
            "tags": ["tag1", "tag2", "tag3"]
        }

    @apiUse UnauthorizedAccessError
    @apiUse ResourceDoesNotExist
    @apiUse BadRequest
    """
    # Parse request into JSON dict
    req = RequestUtil.get_request()

    # Create article
    result = MongoUtil.create_article(req, list_id)

    # If error occurs
    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    if not os.getenv('FLASK_CONFIGURATION') == 'test':
        # Save it to elasticsearch
        ElasticSearchUtil.save_to_es(result)

    app.logger.info('User {} Create article {} in List ID: {}'.format(user, result, list_id))
    return jsonify(JsonUtil.serialize(result)), 200


@app.route('/article/<string:article_id>', methods=['PUT'])
@authorized_required
def update_article(user, article_id):
    """
    @api {put} /article/:id Update a article
    @apiName Update a article
    @apiGroup Article

    @apiUse AuthorizationTokenHeader

    @apiParam {String} title The new article title.
    @apiParam {String} description The new description.
    @apiParam {String} [url] The new url to the article.
    @apiParam {Json} [tags] The new user custom tags.
    @apiParamExample {json} Request (Example):
        {
            "title": "God know what it is",
            "description": "I don't know",
            "url": "https://www.gooel.com/something",
            "tags": ["tag1", "tag2", "tag3"]
        }

    @apiSuccess {json} The new article json data.
    @apiSuccessExample {json} Respond (Example)
        {
            "id": "adlkfdalfjk",
            "title": "God know what it is",
            "description": "I don't know",
            "url": "https://www.gooel.com/something",
            "tags": ["tag1", "tag2", "tag3"]
        }

    @apiUse UnauthorizedAccessError
    @apiUse ResourceDoesNotExist
    @apiUse BadRequest
    """
    # Parse request into JSON dict
    print(request.get_json())
    req = RequestUtil.get_request()
    print(req)
    # Update article
    result = MongoUtil.update_article(req, article_id)

    # If error occurs
    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    # Update in elasticsearch
    if not os.getenv('FLASK_CONFIGURATION') == 'test':
        # Save it to elasticsearch
        ElasticSearchUtil.save_to_es(result)

    app.logger.info('User {} Update article {}'.format(user, result))
    return jsonify(JsonUtil.serialize(result)), 200


@app.route('/group/<string:group_id>/list/<string:list_id>/article', methods=['POST'])
@authorized_required
def create_article_in_group(user, group_id, list_id):
    """
    @api {post} /group/:id/list/:id/article/ Create a article in group
    @apiName Create a article in group
    @apiGroup Article

    @apiUse AuthorizationTokenHeader

    @apiParam {String} title The article title.
    @apiParam {String} description The description.
    @apiParam {String} [url] The url to the article.
    @apiParam {Json} [tags] The user custom tags.
    @apiParamExample {json} Request (Example):
        {
            "title": "God know what it is",
            "description": "I don't know",
            "url": "https://www.gooel.com/something",
            "tags": ["tag1", "tag2", "tag3"]
        }

    @apiSuccess {String} Message Success message.

    @apiUse GroupAccessDenied
    @apiUse ListDoesNotExist
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    # Parse request, parse empty string and
    req = RequestUtil.get_request()

    # Create new article
    result = MongoUtil.create_article_in_group(req, list_id, group_id)

    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    if not os.getenv('FLASK_CONFIGURATION') == 'test':
        # Save it to elasticsearch
        ElasticSearchUtil.save_to_es(result)

    app.logger.info('User {} Create article {} in List ID: {} in Group ID: {}'.format(
        user, result, list_id, group_id))
    return jsonify(JsonUtil.serialize(result)), 200


@app.route('/user/article/<string:article_id>/tag', methods=['POST'])
@authorized_required
def add_tags(user, article_id):
    """
    @api {post} /user/article/:id/tag Add tag to article
    @apiName Add tag to the article
    @apiGroup Article

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id The article id.
    @apiParam {Json} tags The user custom tags.
    @apiParamExample {json} Request (Example):
        {
            "tag": "science"
        }

    @apiSuccess {String} Message Success message.

    @apiUse UnauthorizedAccessError
    @apiUse ListDoesNotExist
    """
    # Get tag from requrest
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    req = RequestUtil.get_request()
    tag = req.get('tag')

    # Add tag
    article = MongoUtil.add_tag(article_id, tag)

    # If the article does not exist
    if article is None:
        return jsonify({
            'msg': 'List does not exist'
        }), 400

    if not os.getenv('FLASK_CONFIGURATION') == 'test':
        # Save it to elasticsearch
        ElasticSearchUtil.save_to_es(article)

    app.logger.info('User {} Add tag {} to {}'.format(user, tag, article))
    return jsonify(JsonUtil.serialize(article)), 200
