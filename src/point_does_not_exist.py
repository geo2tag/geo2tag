from base_geo2tag_exception import BaseGeo2TagException

class PointDoesNotExist(BaseGeo2TagException):

    def getReturnObject(self):
        ERROR = "Point does not exist"
        return ERROR, 404
