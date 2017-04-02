from app.util import RequestUtil, ResponseUtil, JsonUtil
from app.util.AuthUtil import *


@app.route('/share/list', methods=['POST'])
@authorized_required
def share_list_to_group(user):
    """
    @api {post} /share/list Share list to multiple groups.
    @apiName Share list to multiple groups.
    @apiGroup Share

    @apiUse AuthorizationTokenHeader

    @apiParam {String} list_id: A id of the list to share
    @apiParam {String[]} group_id: The list of group id of the group to share
    @apiParamExample {json} Request (Example)
        {
            "list_id": "asdklfaj",
            "group_id": ["adlskfjldas", "adsfkdasf"]
        }

    @apiUse GroupAccessDenied
    @apiUse ListDoesNotExist
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    # Parse the request body
    req = RequestUtil.get_request()
    group_id = req.get('group_id', None)
    list_id = req.get('list_id', None)

    # Create a duplicate list in the group
    result = MongoUtil.share_list_to_group(user, list_id, group_id)

    # If error occurs
    if isinstance(result, str):
        app.logger.debug(result)
        return ResponseUtil.error_response(result)

    app.logger.info('User {} Share list {} to Group {}'.format(user, list_id, group_id))

    return jsonify(msg='Success'), 200


@app.route('/user/list/<string:base_list_id>/article/<string:article_id>/share/group/<string:group_id>/list'
           '/<target_list_id>', methods=['POST'])
@authorized_required
def share_article_to_group(user, base_list_id, article_id, group_id, target_list_id):
    """
    @api {post} /user/list/:id/article/:id/share/group/:id/list/:id Share a article to group list.
    @apiName Share a article into a group list.
    @apiGroup Share

    @apiUse AuthorizationTokenHeader

    @apiUse UnauthorizedAccessError
    @apiUse ResourceDoesNotExist
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    result = MongoUtil.share_article_to_group_list(user, base_list_id, article_id, group_id, target_list_id)

    if isinstance(result, str):
        app.logger.debug(result)
        return ResponseUtil.error_response(result)

    app.logger.info('User {} share article {} to group {}'.format(user, article_id, group_id))

    return jsonify(msg='Success')
