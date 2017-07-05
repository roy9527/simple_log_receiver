from . import api
from flask import jsonify, request, make_response, send_file
from .. import app
import logging
from logging.handlers import WatchedFileHandler

@api.route('/upload_log', methods=['GET', 'POST'])
def upload_log():
    try:
        data = request.get_json()
        logger = logging.getLogger('gunicorn.access')
        # logger.addHandler(WatchedFileHandler('log/access.log'))
        logger.propagate = False
        # handler = logging.FileHandler('eiffel_flask.log', encoding='UTF-8')
        # handler = WatchedFileHandler('log/access.log')
        # handler.setLevel(logging.INFO)
        # logging_format = logging.Formatter('%(asctime)s - %(funcName)s - %(message)s')
        # handler.setFormatter(logging_format)
        # logger.addHandler(handler)
        logger.info(data)
    except:
        return "{\"r\":\"failed\"}"
    return "{\"r\":\"success\"}"

@api.route('/get_file', methods=['GET'])
def get_file():
    response = make_response(send_file("../assets/a.zip"))
    response.headers["Content-Disposition"] = "attachment; filename=a.zip;"
    return response