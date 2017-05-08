from . import api
from flask import jsonify, request
from .. import app
import logging

@api.route('/upload_log', methods=['GET', 'POST'])
def upload_log():
    try:
        data = request.get_json()
        app.logger.info(data)
    except:
        return "{\"r\":\"failed\"}"
    return "{\"r\":\"success\"}"