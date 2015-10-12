from base_geo2tag_exception import BaseGeo2TagException


class PluginNotEnabledException(BaseGeo2TagException):

    def getReturnObject(self):
        ERROR = "Plugin is not enabled"
        return ERROR, 404
