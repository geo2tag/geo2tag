from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('logSize', type=int, default=1048576)
parser.add_argument('ownerId', type=str, default='STUB')


class ServiceResource(Resource):
    def get(self, serviceName):
        args = parser.parse_args()
        return {serviceName: args}

    def put(self, serviceName):
        args = parser.parse_args()
        return {serviceName: args}

    def delete(self, serviceName):
        args = parser.parse_args()
        return {serviceName: args}  

class ServiceListResource(Resource):
    def post(self):
    	parser = reqparse.RequestParser()
        args = parser.parse_args()