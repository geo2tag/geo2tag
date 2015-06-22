class ChannelDoesNotExist(Exception):
    def getReturnObject(self):
        ERROR = "Channel does not exist"
        return ERROR, 404