from flask.ext.restful import Resource
from db_model import getServiceIdByName, updateService, removeService
from possible_exception import possibleException
from service_parsers import ServiceParser

SRV_NAME_DISCR = 'Service description'
SRV_NAME_UPD = 'Service updated'
SRV_NAME_RM = 'Service removed'

ARGS_NAME = "name"
ARGS_LOG_SIZE = "logSize"
ARGS_OWNER_ID = "ownerId"


class ServiceResource(Resource):

    @possibleException
    def get(self, serviceName):
        getServiceResult = getServiceIdByName(serviceName)
        return getServiceResult

    @possibleException
    def put(self, serviceName):
        parserList = ServiceParser.parsePutParameters()
        updateService(serviceName, parserList)
        return {serviceName: SRV_NAME_UPD}

    @possibleException
    def delete(self, serviceName):
        removeService(serviceName)
        return {serviceName: SRV_NAME_RM}
