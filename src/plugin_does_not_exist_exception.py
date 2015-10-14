from base_geo2tag_exception import BaseGeo2TagException


class PluginDoesNotExistException(BaseGeo2TagException):
    pluginName = 'pluginName'

    def __init__(self, plugin):
        self.pluginName = plugin

    def getReturnObject(self):
        ERROR = "Plugin does not exist " + self.pluginName
        return ERROR, 404
