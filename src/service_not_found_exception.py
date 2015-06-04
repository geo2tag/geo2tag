class ServiceNotFoundException(Exception):
    def getReturnObject(self):
          ERROR = 'Service not found'
          return ERROR, 400