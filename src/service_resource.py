from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from db_model import addService, getServiceIdByName
from  service_not_found_exception import ServiceNotFoundException
from bson.json_util import dumps
from service_parsers import ServiceParser
import json

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
            print type(getServiceResult)
        except ServiceNotFoundException as e:
            return e.getReturnObject()
        print type(getServiceResult)
        return getServiceResult

    def put(self, serviceName):
        parserList = ServiceParser.parsePutParameters()
        return {serviceName: SRV_NAME_UPD}

    def delete(self, serviceName):
        return {serviceName: SRV_NAME_RM} 
