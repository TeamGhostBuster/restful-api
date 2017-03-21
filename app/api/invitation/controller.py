from app.util import JsonUtil, RequestUtil, ResponseUtil, MongoUtil
from app.util.AuthUtil import *


@app.route('/group/<string:group_id>/invite', methods=['POST'])
@authorized_required
def invite_user_to_group(user, group_id):
    """
    @api {post} /group/:id/invite Invite user to a group
    @apiName invite user to a group
    @apiGroup Invitation

    @apiUse AuthorizationTokenHeader

    @apiParam {String[]} user_email A list of invitees' email.
    @apiParamExample {json} Request(Example)
        {
            "email": ["invitee@ualberta.ca", "invitee2@ualberta.ca"]
        }

    @apiSuccessExample {json} Response (Example):
        {
            "msg": "Success"
        }

    @apiUse UnauthorizedAccessError
    @apiUse UserHasInvited
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    req = RequestUtil.get_request()
    email = req.get('email', None)

    # Invite user
    result = MongoUtil.invite_user(user, email, group_id)

    # If error occurs
    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    app.logger.info('User {} invite {} to Group {}'.format(user, email, group_id))

    return jsonify(msg='Success'), 200


@app.route('/user/invitation', methods=['GET'])
@authorized_required
def get_user_pending_invitation(user):
    """
    @api {get} /user/invitation Get user pending invitation
    @apiName Get user pending invitation
    @apiGroup Invitation

    @apiUse AuthorizationTokenHeader

    @apiSuccessExample {json} Response (Example):
        {
            "invitation": [
                {   
                    "id": "dalskfsa",
                    "inviter": {
                        "email": "sombody@ualberta.ca",
                        "last_name": "Doe",
                        "first_name": "John"
                    },
                    "group": {
                        "id": "adlksfjsa",
                        "name": "adkslfj"
                    }
                }
            ]
        }

    @apiUse UnauthorizedAccessError
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    result = MongoUtil.get_user_pending_invitation(user)

    # If error occurs
    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    return jsonify(invitation=[JsonUtil.serialize(i, only=('id', 'inviter', 'group')) for i in result]), 200


@app.route('/user/invitation/<string:invitation_id>/accept', methods=['PUT'])
@authorized_required
def accept_invitation(user, invitation_id):
    """
    @api {put} /user/invitation/:id/accept Accept pending invitation.
    @apiName Accept pending invitation.
    @apiGroup Invitation

    @apiUse AuthorizationTokenHeader

    @apiSuccessExample {json} Response (Example):
        {
            "msg": "Success"
        }

    @apiUse BadRequest
    @apiUse ResourceDoesNotExist
    @apiUse UnauthorizedAccessError
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    result = MongoUtil.accept_invitation(user, invitation_id)

    # If error occurs
    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    app.logger.info('User {} accept invitation to Group {}'.format(user, result.group))

    return jsonify(msg='Success accepts invitation'), 200


@app.route('/user/invitation/<string:invitation_id>/deny', methods=['PUT'])
@authorized_required
def deny_invitation(user, invitation_id):
    """
    @api {put} /user/invitation/:id/deny Deny pending invitation.
    @apiName Deny pending invitation.
    @apiGroup Invitation

    @apiUse AuthorizationTokenHeader

    @apiSuccessExample {json} Response (Example):
        {
            "msg": "Success"
        }

    @apiUse BadRequest
    @apiUse ResourceDoesNotExist
    @apiUse UnauthorizedAccessError
    """
    app.logger.info('User {} Access {}'.format(user, request.full_path))

    result = MongoUtil.deny_invitation(user, invitation_id)

    # If error occurs
    if isinstance(result, str):
        return ResponseUtil.error_response(result)

    app.logger.info('User {} deny invitation to Group {}'.format(user, result.group))

    return jsonify(msg='Success deny invitation'), 200
