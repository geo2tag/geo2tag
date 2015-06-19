class ChannelAlreadyExists(Exception):
    def getReturnObject(self):
        ERROR = "Channel already exists"
        return ERROR, 404