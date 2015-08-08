from base_exception import BaseException


class PointDoesNotExist(BaseException):

    def getReturnObject(self):
        ERROR = "Point does not exist"
        return ERROR, 404
