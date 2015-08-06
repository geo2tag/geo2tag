from base_exception import BaseException


class UserDoesNotExist(BaseException):

    def getReturnObject(self):
        ERROR = "User does not exist"
        return ERROR, 404
