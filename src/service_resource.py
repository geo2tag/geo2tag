from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from pymongo import MongoClient
from config_reader import getHost, getPort, getDbName
#from db_model import removeService, getServiceIdByName, updateService
from  service_not_found_exception import ServiceNotFoundException
from service_parsers import ServiceParser

SRV_NAME_DISCR = 'Service description'
SRV_NAME_UPD = 'Service updated'
SRV_NAME_RM = 'Service removed'

ARGS_NAME = "name"
ARGS_LOG_SIZE = "logSize"
ARGS_OWNER_ID = "ownerId"

def possibleException(func):
    def funcPossibleExeption(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return func(*args, **kwargs)
        except ServiceNotFoundException as e:
            return e.getReturnObject()
    return funcPossibleExeption

class ServiceResource(Resource):
    def get(self, serviceName):
        getServiceResult = getServiceIdByName(serviceName)
        return getServiceResult

    def put(self, serviceName):
        parserList = ServiceParser.parsePutParameters()
        updateService(serviceName)
        return {serviceName: SRV_NAME_UPD}

    def delete(self, serviceName):
        #args = ServiceParser.parsePutParameters()
        removeService(serviceName)
        return {serviceName: SRV_NAME_RM}
