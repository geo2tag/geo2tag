from flask import make_response
class ServiceAlreadyExistsException(Exception):
    def getReturnObject(self):
        ERROR = 'Service already exists'
        return make_response(ERROR, 400)