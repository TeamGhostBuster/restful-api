from flask import make_response, jsonify
from app.util.ErrorMessage import *


def error_response(err_code):
    """
    Create respond object base on given exception code
    :param err_code: The exception name
    :return: The respond object
    """
    if err_code in ERROR_CODE_TO_MSG.keys():
        respond = make_response(jsonify(msg=ERROR_CODE_TO_MSG[err_code][0]))
        respond.status_code = ERROR_CODE_TO_MSG[err_code][1]
    else:
        # Unexpected exception occurs
        respond = make_response(jsonify(msg='Server Internal Error'))
        respond.status_code = 500

    return respond
