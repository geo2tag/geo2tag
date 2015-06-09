from flask import make_response
class ServiceNotFoundException(Exception):
    def getReturnObject(self):
          ERROR = 'Service not found'
          return make_response(ERROR, 400)