from base_exception import BaseException

class ChannelAlreadyExists(BaseException):
    def getReturnObject(self):
        ERROR = "Channel already exists"
        return ERROR, 404
