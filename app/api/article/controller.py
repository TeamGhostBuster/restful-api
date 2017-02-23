from app.util import JsonUtil
from app.util import MongoUtil
from app.util import ElasticSearchUtil
from app.util.AuthUtil import *


@app.route('/user/article/<string:article_id>', methods=['GET'])
@authorized_required
def get_article(user, article_id):
    """
    @api {get} /user/article/:id Get a article
    @apiName Get a article
    @apiGroup Article

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id Article unique ID (Required).

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
    # Find article from the database
    article = MongoUtil.find_article(article_id)

    # If the article does not exist
    if article is None:
        return jsonify(msg='Articles does not exist'), 404

    app.logger.info('User {} Get article {}'.format(user, article))
    return jsonify(JsonUtil.serialize(article)), 200


@app.route('/user/article', methods=['POST'])
@authorized_required
def create_article(user):
    """
    @api {post} /user/article/ Create a article
    @apiName Create a article
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

    # If the list does not exist
    if new_article is None:
        return jsonify({
            'msg': 'List does not exist'
        }), 400

    # Save it to elasticsearch
    ElasticSearchUtil.save_to_es(new_article)

    app.logger.info('User {} Create article {} in List ID: {}'.format(user, new_article, list_id))
    return jsonify(JsonUtil.serialize(new_article)), 200


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
    req = request.get_json()
    tag = req.get('tag')

    # Add tag
    article = MongoUtil.add_tag(article_id, tag)

    # If the article does not exist
    if article is None:
        return jsonify({
            'msg': 'List does not exist'
        }), 400

    # Save it to elasticsearch
    ElasticSearchUtil.save_to_es(article)

    app.logger.info('User {} Add tag {} to {}'.format(user, tag, article))
    return jsonify(JsonUtil.serialize(article)), 200
