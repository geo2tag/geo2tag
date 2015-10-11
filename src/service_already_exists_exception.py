from base_geo2tag_exception import BaseGeo2TagException

class ServiceAlreadyExistsException(BaseGeo2TagException):

    def getReturnObject(self):
        ERROR = 'Service already exists'
        return ERROR, 400
