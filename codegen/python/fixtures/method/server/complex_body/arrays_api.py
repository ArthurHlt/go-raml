# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

from flask import Blueprint
import handlers


arrays_api = Blueprint('arrays_api', __name__)


@arrays_api.route('/arrays', methods=['POST'])
def arrays_post():
    """
    handle array
    It is handler for POST /arrays
    """
    return handlers.arrays_postHandler()


@arrays_api.route('/arrays', methods=['PUT'])
def arrays_put():
    """
    another form of array
    It is handler for PUT /arrays
    """
    return handlers.arrays_putHandler()
