from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse


class ServiceResource(Resource):
    def get(self, serviceName):
        return {serviceName: 'Service description'}

    def put(self, serviceName):
        return {serviceName: 'Service updated'}

    def delete(self, serviceName):
        return {serviceName: 'Service removed'}

def parser():
    parser = reqparse.RequestParser()
    parser.add_argument('number', type=int, default=None)
    parser.add_argument('offset', type=int, default=None)
    args = parser.parse_args()
    return args
