from flask_restful import reqparse
from flask.ext.restful import Resource
from flask import request
AUTHORIZED_URL = '/login/google/authorized' 

class LoginGoogleAuthorizedResource(Resource):
    def post(self):
        return request.data
