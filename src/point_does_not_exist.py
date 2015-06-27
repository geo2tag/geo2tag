class PointDoesNotExist(Exception):
    def getReturnObject(self):
        ERROR = "Point does not exist"
        return ERROR, 404