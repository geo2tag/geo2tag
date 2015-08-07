from base_exception import BaseException


class AuthorizationError(BaseException):

    def getReturnObject(self):
        ERROR = "Authorization error"
        return ERROR, 401
