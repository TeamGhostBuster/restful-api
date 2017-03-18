from app.util import JsonUtil, RequestUtil, ResponseUtil
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

    @apiParam {String} name Group name.
    @apiParam {String[]} [members] A list of member email.
    @apiParam {String} [description] description.
    @apiParamExample {json} Request (Example)
        {
            "name": "CMPUT495 Seminar",
            "members": ["test@ualberta.ca", "abc@ualberta.ca"],
            "description": "Group for CMPUT495 Seminar"
        }
    
    @apiSuccessExample {json} Response (Example):
        {
            "description": null,
            "id": "58cc4f6ac6091e84d0db5c1d",
            "lists": [],
            "members": [
                {
                    "first_name": "Zichun",
                    "id": "58cc4e32c6091e83c8611208",
                    "last_name": "Lin"
                },
                {
                    "first_name": "Michael",
                    "id": "58cc4da5c6091e83605ae5af",
                    "last_name": "Lin"
                }
            ],
            "moderator": {
                "first_name": "Zichun",
                "id": "58cc4e32c6091e83c8611208",
                "last_name": "Lin"
            },
            "name": "Group #4"
        }
        
    @apiUse UnauthorizedAccessError
    @apiUse ResourceDoesNotExist
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    # Get group name + group parameters from api
    req = RequestUtil.get_request()
    group_name = req.get('name')
    members = req.get('members', None)
    description = req.get('description', None)

    # Create new group
    result = MongoUtil.create_group(group_name, user, members, description)

    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    app.logger.info('User {} created group'.format(user, result))

    return jsonify(JsonUtil.serialize(result)), 200


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

    @apiParam {String} member_email: member's email
    @apiParamExample {json} Request (Example)
        {
            "member_email": "test@ualbeta.ca"
        }

    @apiUse UnauthorizedAccessError
    @apiUse ResourceDoesNotExist
    """
    req = RequestUtil.get_request()
    member_email = req.get('member_email')

    result = MongoUtil.add_group_member(group_id, member_email)

    # If error occurs
    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    app.logger.info('User {} add member {} to {}'.format(user, member_email, result))

    return jsonify(JsonUtil.serialize(result)), 200


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
