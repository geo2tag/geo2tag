from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from db_model import addService, getServiceIdByName
from  service_not_found_exception import ServiceNotFoundException
from bson.json_util import dumps

SRV_NAME_DISCR = 'Service description'
SRV_NAME_UPD = 'Service updated'
SRV_NAME_RM = 'Service removed'

ARGS_NAME = "name"
ARGS_LOG_SIZE = "logSize"
ARGS_OWNER_ID = "ownerId"

class ServiceResource(Resource):
    def get(self, serviceName):
        try:
            getServiceResult = getServiceIdByName(serviceName)
        except ServiceNotFoundException as e:
            return e.getReturnObject()
        return dumps(getServiceResult, ensure_ascii=False).encode('utf8')

    def put(self, serviceName):
        parserList = parsePut()
        return {serviceName: SRV_NAME_UPD}

    def delete(self, serviceName):
        parserList = parse()
        return {serviceName: SRV_NAME_RM} 

def parse():
    parser = reqparse.RequestParser()
    parser.add_argument(ARGS_NAME, type=str, required=True)
    parser.add_argument(ARGS_LOG_SIZE, type=int, default=1048576)
    parser.add_argument(ARGS_OWNER_ID, type=str, default='STUB')
    args = parser.parse_args()
    return args

def parsePut():
    parser = reqparse.RequestParser()
    parser.add_argument(ARGS_LOG_SIZE, type=int, required=True)
    args = parser.parse_args()
    return args