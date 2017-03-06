from app.util.AuthUtil import *
from app.util import JsonUtil, ResponseUtil, MongoUtil


@app.route('/group/<string:group_id>/list/<string:list_id>/article/<string:article_id>/upvote', methods=['POST'])
@authorized_required
def upvote_article(user, group_id, list_id, article_id):
    """
    @api {post} /group/:id/list/:id/article/:id/upvote Upvote an article in group
    @apiName Upvote an article in group
    @apiGroup Vote

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id Vote object's unique ID.

    @apiUse UnauthorizedAccessError
    @apiUse ResourceDoesNotExist
    @apiUse BadRequest
    @apiUse UserHasVoted
    """
    # Upvote the article
    result = MongoUtil.upvote_article(user, group_id, list_id, article_id)

    # If there is error occurs
    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    return jsonify(JsonUtil.serialize(result, only=('article', 'list', 'vote_count'))), 200


@app.route('/group/<string:group_id>/list/<string:list_id>/article/<string:article_id>/downvote', methods=['POST'])
@authorized_required
def downvote_article(user, group_id, list_id, article_id):
    """
    @api {post} /group/:id/list/:id/article/:id/downvote Downvote an article in group
    @apiName Downvote an article in group
    @apiGroup Vote

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id Vote object's unique ID.

    @apiSuccess {Integer} vote_count The total vote count
    @apiSuccess {Object} list The list associate with this vote
    @apiSuccess {String} list.id The id of the list associates with this vote
    @apiSuccess {Object} article The article associate with this vote
    @apiSuccess {String} list.id The id of the article associates with this vote
    @apiSuccessExample {json} Response (Example)
        {
            "vote_count": 2,
            "list": {
                "id": "ajsdklfdas"
            },
            "article: {
                "id": "dajlkfaskl"
            }
        }

    @apiUse UnauthorizedAccessError
    @apiUse ResourceDoesNotExist
    @apiUse BadRequest
    @apiUse UserHasVoted
    """
    # Downvote the article
    result = MongoUtil.downvote_article(user, group_id, list_id, article_id)

    # If there is error occurs
    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    return jsonify(JsonUtil.serialize(result, only=('article', 'list', 'vote_count'))), 200
