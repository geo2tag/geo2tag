from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
#from db_model import addService

class ServiceResource(Resource):
    def get(self, serviceName):
        parserList = parse()
        return {serviceName: 'Service description'}

    def put(self, serviceName):
        parserList = parse()
        return {serviceName: 'Service updated'}

    def delete(self, serviceName):
        parserList = parse()
        return {serviceName: 'Service removed'} 

class ServiceListResource(Resource):
    def post(self):
        listAgrs = parse()
        #addService(listAgrs.get('name', 0), listAgrs.get('logSize', 0), listAgrs.get('ownerId', 0))

def parse():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('logSize', type=int, default=1048576)
    parser.add_argument('ownerId', type=str, default='STUB')
    args = parser.parse_args()
    return args