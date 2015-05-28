from service_resource import parse

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
        
