from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse

class LogResource(Resource):
    def get(self, serviceName):
        parser_dict = parse()
        return {serviceName: 'Service description'}

    def put(self, serviceName):
        parser_dict = parse()
        return {serviceName: 'Service updated'}

    def delete(self, serviceName):
        parser_dict = parse()
        return {serviceName: 'Service removed'} 

def parse():
    parser = reqparse.RequestParser()
    parser.add_argument('number', type=int, default=None)
    parser.add_argument('offset', type=int, default=None)
    parser.add_argument('date_from', type=datetime, default=None)
    parser.add_argument('date_to', type=datetime, default=None)
    args = parser.parse_args()
    return args

 
