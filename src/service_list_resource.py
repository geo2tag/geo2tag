from possible_exception import possibleException
from flask_restful import Resource
from db_model import addService, getServiceList
from bson.json_util import dumps
from service_list_parsers import ServiceListParser, GET_ARGS_NUMBER, \
    GET_ARGS_OFFSET, POST_ARGS_NAME, POST_ARGS_LOG_SIZE, \
    POST_ARGS_OWNER_ID, DEFAULT_OWNER_ID, GET_ARGS_SUBSTR, \
    GET_ARGS_OWNER_ID


class ServiceListResource(Resource):

    @possibleException
    def get(self):
        args = ServiceListParser.parseGetParameters()
        number = args[GET_ARGS_NUMBER]
        offset = args[GET_ARGS_OFFSET]
        substring = args[GET_ARGS_SUBSTR]
        ownerId = args[GET_ARGS_OWNER_ID]
        serviceList = getServiceList(number, offset, substring, ownerId)
        return serviceList

    @possibleException
    def post(self):
        listAgrs = ServiceListParser.parsePostParameters()
        result = addService(listAgrs.get(POST_ARGS_NAME), listAgrs.get(
            POST_ARGS_LOG_SIZE), listAgrs.get(POST_ARGS_OWNER_ID))
        return dumps(result, ensure_ascii=False).encode('utf8')
