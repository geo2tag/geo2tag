from base_geo2tag_exception import BaseGeo2TagException


class AuthorizationError(BaseGeo2TagException):

    def getReturnObject(self):
        ERROR = "Authorization error"
        return ERROR, 401
