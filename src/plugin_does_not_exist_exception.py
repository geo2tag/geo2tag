from base_exception import BaseException

class PluginDoesNotExistException(BaseException):
    pluginName = 'pluginName'
    def __init__(self, plugin):
        self.pluginName = plugin
    def getReturnObject(self):
        ERROR = "Plugin does not exist " + self.pluginName
        return ERROR, 404
