from app.util import JsonUtil, RequestUtil
from app.util.AuthUtil import *


@app.route('/group/<string:group_id>', methods=['GET'])
@group_read_permission_required
def get_group_info(user, group_id):
    """
    @api {get} /group/:id Get info of group
    @apiName Get group information
    @apiGroup Group

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id Group unique ID.

    @apiSuccess {String} id The id of the group.
    @apiSuccess {String} name The group's name.
    @apiSuccess {String} description A short description of the group.
    @apiSuccess {Object[]} moderator The Group moderator.
    @apiSuccess {String} moderator.id The moderator's id.
    @apiSuccess {String} moderator.first_name The moderator's first name.
    @apiSuccess {String} moderator.last_name the moderator's last name.
    @apiSuccess {Object[]} members Group members' data.
    @apiSuccess {String} members.id The member's id.
    @apiSuccess {String} members.first_name The member's first name.
    @apiSuccess {String} members.last_name The member's last name.
    @apiSuccess {Object[]} lists The group's lists.
    @apiSuccess {String} lists.id The list's id.
    @apiSuccess {String} lists.name The list's name.
    @apiSuccessExample {json} Response (Example):
        {
            "id": "31ladsjfl",
            "name": "CMPUT 391 Seminar",
            "description": "Reading Group for CMPUT 391 Seminar."
            "moderator": {
                    "id": "adlfajdls",
                    "first_name": "Ricardo",
                    "last_name": "Sanchez"
            },
            "members": [
                {
                    "id": "adlfajdls",
                    "first_name": "Ricardo",
                    "last_name": "Sanchez"
                }
            ],
            "lists": [
                {
                    "id": "adlasfdls",
                    "name": "Data Storage Reading List"
                }
            ]
        }

    @apiUse GroupAccessDenied
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    reading_group = MongoUtil.find_group(group_id)

    # Check for bad group
    if reading_group is None:
        return jsonify(msg='Group does not exist.'), 404

    # Convert the group into JSON format
    return jsonify(JsonUtil.serialize(reading_group)), 200


@app.route('/group', methods=['POST'])
@authorized_required
def create_group(user):
    """
    @api {post} /group Create a reading group
    @apiName Create a reading group
    @apiGroup Group

    @apiHeader {String} Access-Token Access token obtains from Oauth2 provider.
    @apiHeader {String} Provider-Name Oauth2 provider name.
    @apiHeaderExample {json} Header (Example):
        {
            "Access-Token": "12xsdklajlkadsf",
            "Provider-Name": "Google"
        }

    @apiParam {String} name Group name
    @apiParam {String} [members[ comma-separated string of member IDs
    @apiParam {String} [description] description
    @apiParamExample {json} Request (Example)
        {
            "name": "CMPUT495 Seminar",
            "members": "58acbd4485ed06eb52a80a5f,58abcd4345ed06fb52a91a5e"
            "description": "Group for CMPUT495 Seminar"
        }

    @apiUse UnauthorizedAccessError
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    # Get group name + group parameters from api
    req = RequestUtil.get_request()
    group_name = req.get('name')
    moderator = user
    members = req.get('members', None)

    # Only split if it is not None
    if members is not None:
        members = members.split(',')
    description = req.get('description', None)

    # Check for missing parameters
    if group_name is None:
        return jsonify(msg='Bad Request'), 400

    new_group = MongoUtil.create_group(group_name, moderator, members, description)

    app.logger.info('User {} created group'.format(user, new_group))

    return jsonify(JsonUtil.serialize(new_group)), 200


@app.route('/group/<string:group_id>/members', methods=['POST'])
@authorized_required
def add_group_member(user, group_id):
    """
    @api {post} /group/:id/members Add a new member to reading group
    @apiName Add a new member to a reading groups
    @apiGroup Group

    @apiHeader {String} Access-Token Access token obtains from Oauth2 provider.
    @apiHeader {String} Provider-Name Oauth2 provider name.
    @apiHeaderExample {json} Header (Example):
        {
            "Access-Token": "12xsdklajlkadsf",
            "Provider-Name": "Google"
        }

    @apiParam {String} member_id: member ID
    @apiParamExample {json} Request (Example)
        {
            "member_id": "58acbd42a80a5f"
        }

    @apiUse UnauthorizedAccessError
    """
    req = RequestUtil.get_request()
    member_id = req.get('member')

    reading_group = MongoUtil.add_group_member(group_id, member_id)

    # Check for valid group
    if reading_group is None:
        return jsonify(msg='Group does not exist.'), 400

    app.logger.info('User {} add member {} to {}'.format(user, member_id, reading_group))

    return jsonify(JsonUtil.serialize(reading_group)), 200


@app.route('/group/list/<string:list_id>/archive', methods=['DELETE'])
@group_read_permission_required
def archive_group_list(user, list_id):
    """
    @api {delete} /group/list/:id/archive Archive a group list
    @apiName Archive a group list
    @apiGroup Group

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id The list id.
    @apiParam {String} group_id The group id.
    @apiParamExample {json} Request (Example)
        {
            "group_id": "adlfkjalsk"
        }

    @apiSuccess {String} id Group id
    @apiSuccess {String} name Group name
    @apiSuccess {String} description Group description
    @apiSuccess {Object[]} lists Lists data
    @apiSuccess {String} lists.id List id
    @apiSuccess {Boolean} lists.archived Archived list or not
    @apiSuccess {String} lists.name List name
    @apiSuccessExample {json} Response (Example):
        {
            "id": "31ladsjfl",
            "name": "Seminar",
            "lists": [
                {
                    "id": "adlfajdls",
                    "archived": "True",
                    "name": "Process"
                }
            ]
        }

    @apiUse GroupAccessDenied
    @apiUse ListDoesNotExist
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    # Parse request
    req = RequestUtil.get_request()
    group_id = req.get('group_id')

    # Archive the list in the group
    group = MongoUtil.archive_group_list(group_id, list_id)

    # If the user does not have permission or list does not exist
    if group is None:
        return jsonify(msg='List does not exist'), 404

    app.logger.info('User {} Achieve List ID: {} in Group '.format(user, list_id, group))
    return jsonify(JsonUtil.serialize(group, only=('id', 'name', 'description', 'lists')))


@app.route('/group/list/<string:list_id>/retrieve', methods=['PUT'])
@group_read_permission_required
def retrieve_group_list(user, list_id):
    """
    @api {delete} /group/list/:id/retrieve Retrieve a group list
    @apiName Retrieve a group list
    @apiGroup Group

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id The list id.
    @apiParam {String} group_id The group id.
    @apiParamExample {json} Request (Example)
        {
            "group_id": "adlfkjalsk"
        }

    @apiSuccess {String} id Group id
    @apiSuccess {String} name Group name
    @apiSuccess {String} description Group description
    @apiSuccess {Object[]} lists Lists data
    @apiSuccess {String} lists.id List id
    @apiSuccess {Boolean} lists.archived Archived list or not
    @apiSuccess {String} lists.name List name
    @apiSuccessExample {json} Response (Example):
        {
            "id": "31ladsjfl",
            "name": "dasjflk",
            "description": "adlskfsa",
            "lists": [
                {
                    "id": "adlfajdls",
                    "archived": "False",
                    "name": "Process"
                }
            ]
        }

    @apiUse GroupAccessDenied
    @apiUse ListDoesNotExist
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    # Parse request
    req = RequestUtil.get_request()
    group_id = req.get('group_id')

    # Retrieve the list in the group
    group = MongoUtil.retrieve_group_list(group_id, list_id)

    # If the user does not have permission or list does not exist
    if group is None:
        return jsonify(msg='List does not exist'), 404

    app.logger.info('User {} Retrieve List ID: {} in Group '.format(user, list_id, group))
    return jsonify(JsonUtil.serialize(group, only=('id', 'name', 'description', 'lists')))
