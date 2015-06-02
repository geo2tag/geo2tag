from flask_restful import reqparse
from flask.ext.restful import Resource
from db_model import addService, getServiceList
from service_resource import parse

class ServiceListResource(Resource):

    def get(self):
        args = parser()
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
        listAgrs = parse()
        result = addService(listAgrs.get('name'), listAgrs.get('logSize'), listAgrs.get('ownerId'))
        if result is None:
            return  'Service already exists', 400
        return result
        
def parser():
    parser = reqparse.RequestParser()
    parser.add_argument('number', type=int, default=None)
    parser.add_argument('offset', type=int, default=None)
    args = parser.parse_args()
    return args
