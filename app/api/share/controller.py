from app import app

from app.util.AuthUtil import *
from app.util import JsonUtil
from flask import request


@app.route('/share/list', methods=['POST'])
@group_read_permission_required
def share_list_to_group(user):
    """
    @api {post} /share/list Share list to group
    @apiName Share list to group
    @apiGroup Group

    @apiUse AuthorizationTokenHeader

    @apiParam {String} list_id: The list id of the list to share
    @apiParam {String} group_id: The group id of the group to share
    @apiParamExample {json} Request (Example)
        {
            "list_id": "aldksfjalsdk",
            "group_id": "adlskfjldas"
        }

    @apiUse GroupAccessDenied
    @apiUse ListDoesNotExist
    """
    # Parse the request body
    req = request.get_json()
    group_id = req.get('group_id', None)
    list_id = req.get('list_id', None)

    # Chceck parameter
    if list_id is None or group_id is None:
        return jsonify(msg='Bad Request'), 400

    # Create a duplicate list in the group
    duplicate_list = MongoUtil.share_list_to_group(user, list_id, group_id)

    # List does not exist or list is not owned by the user
    if duplicate_list is None:
        return jsonify(msg='List does not exist'), 401

    app.logger.info('User {} Share list {} to Group {}'.format(user, list_id, group_id))
    return jsonify(JsonUtil.serialize(duplicate_list))
