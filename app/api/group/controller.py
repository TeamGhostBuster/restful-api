from app.util import MongoUtil
from app.util.AuthUtil import *
from app.util import JsonUtil


@app.route('/group/<string:group_id>', methods=['GET'])
@authorized_required
def get_group_info(user, group_id):
    """
    @api {get} /group/:id Get info of group
    @apiName Get group information
    @apiGroup Group

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id Group unique ID.

    @apiSuccess {String} Group id.
    @apiSuccess {String} Group name.
    @apiSuccess {String} Group description
    @apiSuccess {Object[]} Group moderator.
        @apiSuccess {String} Group moderator id.
        @apiSuccess {String} Group moderator first name.
        @apiSuccess {String} Group moderator last name.
    @apiSuccess {Object[]} Group members.
        @apiSuccess {String} Group member id.
        @apiSuccess {String} Group member first name.
        @apiSuccess {String} Group member last name.
    @apiSuccess {Object[]} Group lists.
        @apiSuccess {String} List id.
        @apiSuccess {String} List name.
    @apiSuccessExample {json} Response (Example):
        {
            "id": "31ladsjfl",
            "name": "CMPUT 391 Seminar",
            "description": "Reading Group for CMPUT 391 Seminar."
            "moderator": {
                    "id": "adlfajdls",
                    "first_name": "Jesus",
                    "last_name": "Sanchez
            },
            "members": [
                {
                    "id": "adlfajdls",
                    "first_name": "Jesus",
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

    @apiUse UnauthorizedAccessError
    """
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

    @apiParam {String} name: group_name
    @apiParam {String} members: comma-separated string of member IDs
    @apiParam {String} description: description
    @apiParamExample {json} Request (Example)
        {
            "name": "CMPUT495 Seminar",
            "members": "58acbd4485ed06eb52a80a5f,58abcd4345ed06fb52a91a5e"
            "description": "Group for CMPUT495 Seminar"
        }

    @apiUse UnauthorizedAccessError
    """
    # Get group name + group parameters from api
    req = request.get_json()
    group_name = req['name']
    moderator = user
    members = req.get('members').split(',')
    description = req.get('description')

    # Check for missing parameters
    if group_name is None:
        return jsonify(msg='Bad Request'), 400

    new_group = MongoUtil.create_group(group_name, moderator, members, description)

    app.logger.info('User {} created group'.format(user, new_group))

    return jsonify(JsonUtil.serialize(new_group)), 200


@app.route('/group/<string:group_id>/members', methods=['POST'])
@authorized_required
def add_group_member(user, group_id):
    req = request.get_json()
    member_id = req.get('member')
    reading_group = MongoUtil.add_group_member(group_id, member_id)

    # Check for valid group
    if reading_group is None:
        return jsonify(msg='Group does not exist.'), 400

    app.logger.info('User {} add member {} to {}'.format(user, member_id, reading_group))

    return jsonify(JsonUtil.serialize(reading_group)), 200
