from app.util import MongoUtil
from app.util.AuthUtil import *
from app.util import JsonUtil


# @app.route('/vote/<string:vote_id>', methods=['GET'])
# @authorized_required
# def get_vote_count(user, vote_id):
#     pass


@app.route('/vote/<string:vote_id>', methods=['GET'])
@authorized_required
def get_vote_object(user, vote_id):
    """
    @api {get} /vote/:id Get vote object
    @apiName Get vote object
    @apiGroup Vote

    @apiUse AuthorizationTokenHeader

    @apiParam {String} id Vote object's unique ID.

    @apiSuccess {String} id Unique vote object id.
    @apiSuccess {Integer} vote_count Number of votes for a vote object.
    @apiSuccess {Object[]} article The article the vote object references.
    @apiSuccess {String} article.id Article ID.
    @apiSuccess {String} article.title Article title.
    @apiSuccess {Object[]} list The list the vote object references.
    @apiSuccess {String} list.id The list's ID.
    @apiSuccess {String} list.name The name of the list.

    @apiSuccessExample {json} Response (Example):
        {
            "id": "58af5d8bc05d63748e93ceec",
            "vote_count": -2,
            "article": {
                "id": "58af4659c05d636a7bf22793",
                "title": "Totally Not Software Processes"
            },
            "list": {
                "id": "58adf7ff0e7cfa33699f29bc",
                "name": "CMPUT404 Reading List"
            }
        }

    @apiUse UnauthorizedAccessError
    """
    # Get the vote object
    vote_object = MongoUtil.find_vote(vote_id)

    # Check for None
    if vote_object is None:
        return jsonify(msg="Vote object does not exist."), 404

    return jsonify(JsonUtil.serialize(vote_object)), 200


@app.route('/vote/<string:vote_id>', methods=['POST'])
@authorized_required
def add_vote(user, vote_id):
    """
    @api {post} /vote/:id Add a group member's vote to the vote object
    @apiName Add a group member's vote to the vote object
    @apiGroup Vote

    @apiHeader {String} Access-Token Access token obtains from Oauth2 provider.
    @apiHeader {String} Provider-Name Oauth2 provider name.
    @apiHeaderExample {json} Header (Example):
        {
            "Access-Token": "12xsdklajlkadsf",
            "Provider-Name": "Google"
        }

    @apiParam {String} upvote Set to either 1 (for upvote) or 0 (for downvote)
    @apiParamExample {json} Request (Example)
        {
            "upvote": "1"
        }

    @apiUse UnauthorizedAccessError
    """
    # Get upvote boolean value from request
    req = request.get_json()
    upvote = bool(int(req['upvote']))

    vote_object = MongoUtil.add_vote(vote_id, upvote, user)

    if vote_object is None:
        return jsonify(msg="Bad request."), 404

    return jsonify(JsonUtil.serialize(vote_object)), 200
