class ServiceAlreadyExistsException(Exception):
    def getReturnObject(self):
        ERROR = 'Service already exists'
        return ERROR, 400