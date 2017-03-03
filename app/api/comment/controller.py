from flask import jsonify, request

from app import app
from app.util import MongoUtil, JsonUtil, RequestUtil, ResponseUtil
from app.util.AuthUtil import authorized_required, validate_id


@app.route('/article/<string:article_id>/comment', methods=['POST'])
@authorized_required
def add_comment(user, article_id):
    """
    @api {post} /article/:id/comment Post comment to an article
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
    @apiUse ResourceDoesNotExist
    @apiUse BadRequest
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    # Get request body
    req = RequestUtil.get_request()
    comment = req.get('comment')
    public = req.get('public')

    # Add comment
    result = MongoUtil.add_comment(user, article_id, comment, public)

    # If error occurs
    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    app.logger.info('User {} Create comment {}'.format(user, result.id))
    return jsonify(JsonUtil.serialize(result))
