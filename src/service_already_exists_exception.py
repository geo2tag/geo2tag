from base_exception import BaseException

class ServiceAlreadyExistsException(BaseException):
    def getReturnObject(self):
        ERROR = 'Service already exists'
        return ERROR, 400
