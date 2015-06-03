from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import addService, getServiceList
from service_parsers import ServiceParser

class ServiceListResource(Resource):

    def get(self):
        args = ServiceParser.parseGetParameters()
        if 'number' in args:
            number = args['number']
        else:
            number = None
        if 'offset' in args:
            offset = args['offset']
        else:
            offset = None
        serviceList = getServiceList(number, offset)
        return serviceList

    def post(self):
        listAgrs = ServiceParser.parsePostParameters()
        result = addService(listAgrs.get('name'), listAgrs.get('logSize'), listAgrs.get('ownerId'))
        if result is None:
            return  "Service already exists", 400
        return result