from base_exception import BaseException


class ChannelDoesNotExist(BaseException):

    def getReturnObject(self):
        ERROR = "Channel does not exist"
        return ERROR, 404
