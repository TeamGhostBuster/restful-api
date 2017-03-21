"""
Python exception and (Response error message, status code) mapping
"""


ERROR_CODE_TO_MSG = {
    'ValidationError': ['Invalid request', 400],
    'DoesNotExist': ['Resource does not exist', 404],
    'InvalidId': ['Invalid request', 404],
    'UserHasVoted': ['User cannot vote twice', 403],
    'NotUniqueError': ['User cannot send invitation twice', 403]
}
