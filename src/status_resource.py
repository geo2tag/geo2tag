from flask import request
from flask.ext.restful import Resource
from flask import make_response

class StatusResource(Resource):
    def get(self):
        return make_response("OK")