from app.util import RequestUtil, ResponseUtil, JsonUtil
from app.util.AuthUtil import *


@app.route('/share/lists', methods=['POST'])
@group_read_permission_required
def share_list_to_group(user):
    """
    @api {post} /share/lists Share list to group
    @apiName Share list to group
    @apiGroup Group

    @apiUse AuthorizationTokenHeader

    @apiParam {String[]} list_id: A list of id of the list to share
    @apiParam {String} group_id: The group id of the group to share
    @apiParamExample {json} Request (Example)
        {
            "list_id": ["aldksfjalsdk", "asdklfaj"],
            "group_id": "adlskfjldas"
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
