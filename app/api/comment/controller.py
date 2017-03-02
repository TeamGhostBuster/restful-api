from flask import jsonify, request

from app import app
from app.util import MongoUtil, JsonUtil, RequestUtil
from app.util.AuthUtil import authorized_required, validate_id


@app.route('/user/article/<string:article_id>/comment', methods=['POST'])
@authorized_required
def add_comment(user, article_id):
    """
    @api {post} /user/article/:id/comment Post comment to an article
    @apiName Post comment to an article
    @apiGroup Comment

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id Article unique ID.
    @apiParam {String} comment The comment to be added
    @apiParam {Boolean} public The privacy setting for the comment, default is True
    @apiParamExample Request (Example)
        {
            "comment": "I hate you",
            "public": "false"
        }

    @apiUse UnauthorizedAccessError
    @apiUse ArticleDoesNotExist
    """
    # Validate the article id
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    if not validate_id(article_id):
        return jsonify(msg='ObjectID is not valid'), 400

    # Get request body
    req = RequestUtil.get_request()
    comment = req.get('comment')
    public = req.get('public')

    new_comment = MongoUtil.add_comment(user, article_id, comment, public)

    if new_comment is None:
        return jsonify(msg='Article does not exist'), 400

    app.logger.info('User {} Create comment {}'.format(user, new_comment.id))

    return jsonify(JsonUtil.serialize(new_comment))


@app.route('/user/list/<string:list_id>/article/<string:article_id>/comment', methods=['GET'])
@authorized_required
def get_comment(user, list_id, article_id):
    """
    @api {get} /user/list/:id/article/:id Get comments of an article
    @apiName Get comments of an article
    @apiGroup Comment

    @apiUse AuthorizationTokenHeader

    @apiSuccessExample {json} Example (Response)
        {
            "comments" : [{
                "id": "afjlkdsfjafla",
                "content": "i hate it",
                "timestamp": "2017-02-04-19-59-59"
            }]
        }

    @apiUse UnauthorizedAccessError
    @apiUse ArticleDoesNotExist
    """
    pass