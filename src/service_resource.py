from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
from service_parsers import ServiceParser

SRV_NAME_DISCR = 'Service description'
SRV_NAME_UPD = 'Service updated'
SRV_NAME_RM = 'Service removed'

ARGS_NAME = "name"
ARGS_LOG_SIZE = "logSize"
ARGS_OWNER_ID = "ownerId"


class ServiceResource(Resource):
    def get(self, serviceName):
        return {serviceName: SRV_NAME_DISCR}

    def put(self, serviceName):
        parserList = ServiceParser.parsePutParameters()
        return {serviceName: SRV_NAME_UPD}

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

def getServiceList(number, offset):
    db = MongoClient(getHost(), getPort())[getDbName()]
    if number is None:
        number = db['services'].count()
    if offset is None:
        offset = 0
    result = list(db['services'].find().sort('name', 1).skip(offset).limit(number))
    return result