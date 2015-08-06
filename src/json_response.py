from flask import make_response
from bson.json_util import dumps


def custom_dumps(data):
    return dumps(data, ensure_ascii=False).encode('utf8')


def buildJsonResponse(data):
    response = make_response(custom_dumps(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.mimetype = 'application/json; charset=utf-8'
    return response
