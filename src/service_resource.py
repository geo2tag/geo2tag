from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from service_parsers import ServiceParser
from db_model import removeService
from  service_not_found_exception import ServiceNotFoundException

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
        #args = ServiceParser.parsePutParameters()
        try:
            removeService(serviceName)
        except ServiceNotFoundException as e:
            return e.getReturnObject()
        return {serviceName: SRV_NAME_RM}