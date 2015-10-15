from base_geo2tag_exception import BaseGeo2TagException

class ChannelDoesNotExist(BaseGeo2TagException):

    def getReturnObject(self):
        ERROR = "Channel does not exist"
        return ERROR, 404
