from flask_restful import reqparse

class ServiceListResource():

    def get(self):
        args = parse()
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
        
def parser():
    parser = reqparse.RequestParser()
    parser.add_argument('number', type=int, default=None)
    parser.add_argument('offset', type=int, default=None)
    args = parser.parse_args()
    return args
