from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from db_model import addService, getServiceIdByName
from  service_not_found_exception import ServiceNotFoundException
from bson.json_util import dumps

class ServiceResource(Resource):
    def get(self, serviceName):
        try:
            getServiceResult = getServiceIdByName(serviceName)
            print getServiceResult
        except ServiceNotFoundException as e:
            return e.getReturnObject()
        return dumps(getServiceResult, ensure_ascii=False).encode('utf8')

    def put(self, serviceName):
        parserList = parsePut()
        return {serviceName: 'Service updated'}

    def delete(self, serviceName):
        parserList = parse()
        return {serviceName: 'Service removed'} 

def parse():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('logSize', type=int, default=1048576)
    parser.add_argument('ownerId', type=str, default='STUB')
    args = parser.parse_args()
    return args

def parsePut():
    parser = reqparse.RequestParser()
    parser.add_argument('logSize', type=int, required=True)
    args = parser.parse_args()
    return args