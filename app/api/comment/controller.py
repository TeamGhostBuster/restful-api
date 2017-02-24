from flask import jsonify

from app import app
from app.util import MongoUtil, JsonUtil, RequestUtil
from app.util.AuthUtil import authorized_required, validate_id


@app.route('/user/article/<string:article_id>/comment', methods=['POST'])
@authorized_required
def add_comment(user, article_id):
    """
    @api {get} /user/article/:id/comment Post comment to an article
    @apiName Post comment to an article
    @apiGroup Article

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
