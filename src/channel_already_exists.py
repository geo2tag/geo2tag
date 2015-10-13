from base_geo2tag_exception import BaseGeo2TagException


class ChannelAlreadyExists(BaseGeo2TagException):

    def getReturnObject(self):
        ERROR = "Channel already exists"
        return ERROR, 400
