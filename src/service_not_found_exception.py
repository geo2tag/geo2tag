from base_exception import BaseException

class ServiceNotFoundException(BaseException):
    def getReturnObject(self):
          ERROR = 'Service not found'
          return ERROR, 404
