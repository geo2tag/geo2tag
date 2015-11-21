from possible_exception import possibleException
from flask_restful import Resource
from db_model import addService, getServiceList
from bson.json_util import dumps
from service_list_parsers import ServiceListParser

GET_ARGS_NUMBER = "number"
GET_ARGS_OFFSET = "offset"
POST_ARGS_NAME = "name"
POST_ARGS_LOG_SIZE = "logSize"
POST_ARGS_OWNER_ID = "ownerId"
DEFAULT_OWNER_ID = 'STUB'
GET_ARGS_SUBSTR = "substring"
SERVICE_ALREADY_EXIST_MSG = "Service already exists"


class ServiceListResource(Resource):

    @possibleException
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
        substring = args[GET_ARGS_SUBSTR]
        serviceList = getServiceList(number, offset, substring)
        return serviceList

    @possibleException
    def post(self):
        listAgrs = ServiceListParser.parsePostParameters()
        result = addService(listAgrs.get(POST_ARGS_NAME), listAgrs.get(
            POST_ARGS_LOG_SIZE), listAgrs.get(POST_ARGS_OWNER_ID))
        return dumps(result, ensure_ascii=False).encode('utf8')
