from possible_exception import possibleException
from flask_restful import Resource
from plugin_config_resource_parser import PluginConfigResourceParser
from plugin_config_reader import PluginConfigReader
from plugin_routines import getPluginList

class PluginConfigResource(Resource):

    @possibleException
    def get(self, pluginName):
        if checkConfigPlugin(pluginName):
            return PluginConfigReader(pluginName).getConfigContent()
        else:
            return 'No plugin config'

    @possibleException
    def put(self, pluginName):
        if checkConfigPlugin(pluginName):
            args = PluginConfigResourceParser.parsePostParameters()
            PluginConfigReader(pluginName).setConfigContent(args)
        else:
            return 'No plugin config'

def checkConfigPlugin(pluginName):
    if pluginName in getPluginList():
        return True
    return False