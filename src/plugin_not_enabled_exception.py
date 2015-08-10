from base_exception import BaseException


class PluginNotEnabledException(BaseException):

    def getReturnObject(self):
        ERROR = "Plugin is not enabled"
        return ERROR, 404
