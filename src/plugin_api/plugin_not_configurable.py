from base_geo2tag_exception import BaseGeo2TagException


class PluginIsNotConfigurable(BaseGeo2TagException):

    def getReturnObject(self):
        ERROR = "No plugin config"
        return ERROR
