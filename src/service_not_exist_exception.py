from base_geo2tag_exception import BaseGeo2TagException


class ServiceNotExistException(BaseGeo2TagException):

    def getReturnObject(self):
        ERROR = 'Service not found'
        return ERROR, 404
