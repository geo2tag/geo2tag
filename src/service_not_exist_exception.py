from base_exception import BaseException


class ServiceNotExistException(BaseException):

    def getReturnObject(self):
        ERROR = 'Service not found'
        return ERROR, 404
