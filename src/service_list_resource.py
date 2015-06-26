from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import addService, getServiceList
from bson.json_util import dumps
from service_list_parsers import ServiceListParser
from service_already_exists_exception import ServiceAlreadyExistsException

GET_ARGS_NUMBER = "number"
GET_ARGS_OFFSET = "offset"
POST_ARGS_NAME = "name"
POST_ARGS_LOG_SIZE = "logSize"
POST_ARGS_OWNER_ID = "ownerId"
DEFAULT_OWNER_ID = 'STUB'
SERVICE_ALREADY_EXIST_MSG = "Service already exists"


class ServiceListResource(Resource):

    def get(self):
        args = ServiceListParser.parseGetParameters()
        if GET_ARGS_NUMBER in args:
            number = args[GET_ARGS_NUMBER]
        else:
            number = None
        if GET_ARGS_OFFSET in args:
            offset = args[GET_ARGS_OFFSET]
        else:
            offset = None
        serviceList = getServiceList(number, offset)
        return serviceList

    def post(self):
        listAgrs = ServiceListParser.parsePostParameters()
        try:
            result = addService(listAgrs.get(POST_ARGS_NAME), listAgrs.get(POST_ARGS_LOG_SIZE), listAgrs.get(POST_ARGS_OWNER_ID))
        except ServiceAlreadyExistsException as e:
            return e.getReturnObject()
        return dumps(result, ensure_ascii=False).encode('utf8')
