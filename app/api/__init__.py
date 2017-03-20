from .article import controller as article_api
from .article import model as article_model
from .comment import controller as comment_api
from .comment import model as comment_model
from .group import controller as group_api
from .group import model as group_model
from .list import controller as list_api
from .list import model as list_model
from .share import controller as share_api
from .user import controller as user_api
from .user import model as user_model
from .vote import controller as vote_api
from .vote import model as vote_model
from .invitation import controller as invitation_api
from .invitation import model as invitation_model

# APIDOC Inherit Doc


"""
@apiDefine AuthorizationTokenHeader
@apiHeader {String} Access-Token Access token obtains from Oauth2 provider.
@apiHeader {String} Provider-Name Oauth2 provider name.
@apiHeaderExample {json} Header (Example):
    {
        "Access-Token": "12xsdklajlkadsf",
        "Provider-Name": "Google"
    }
"""

"""
@apiDefine GroupAccessDenied
@apiError GroupAccessDenied User does not have accesss to the group
@apiErrorExample Error 401
    {
        "msg": "User does not have read permission"
    }
"""

"""
@apiDefine UnauthorizedAccessError
@apiError UnauthorizedAccessError User's access token is not valid
@apiErrorExample Error 401
    {
        "msg": "Unauthorized access"
    }
"""

"""
@apiDefine ListDoesNotExist
apiError ListDoesNotExist The list does not exist
@apiErrorExample Error 404
    {
        "msg": "List does not exist"
    }
"""

"""
@apiDefine ArticleDoesNotExist
apiError ArticleDoesNotExist The article does not exist
@apiErrorExample Error 404
    {
        "msg": "Article does not exist"
    }
"""

"""
@apiDefine InvalidObjectID
apiError ArticleDoesNotExist The article does not exist
@apiErrorExample Error 400
    {
        "msg": "ObjectID is not valid"
    }
"""

"""
@apiDefine UserNotInGroup
apiError UserNotInGroup The user is not in any group
@apiErrorExample Error 204
    {
        "msg": "User is not in any group"
    }
"""

"""
@apiDefine GroupDoesNotExist
@apiError GroupDoesNotExist The group does not exist
@apiErrorExample Error 204
    {
        "msg": "Group does not exist"
    }
"""

"""
@apiDefine ResourceDoesNotExist
@apiError ResourceDoesNotExist The resource does not exist
@apiErrorExample Error 404
    {
        "msg": "Resource does not exist"
    }
"""

"""
@apiDefine BadRequest
@apiError BadRequest The resource does not exist
@apiErrorExample Error 400
    {
        "msg": "Invalid Request"
    }
"""

"""
@apiDefine UserHasVoted
@apiError ResourceDoesNotExist The resource does not exist
@apiErrorExample Error 403
    {
        "msg": "User cannot vote twice"
    }
"""