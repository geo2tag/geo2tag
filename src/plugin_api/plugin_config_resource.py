from possible_exception import possibleException
from flask_restful import Resource
from plugin_config_resource_parser import PluginConfigResourceParser
from plugin_config_reader import PluginConfigReader
from plugin_routines import checkConfigPlugin


class PluginConfigResource(Resource):

    @possibleException
    def get(self, pluginName):
        checkConfigPlugin(pluginName)
        return PluginConfigReader(pluginName).getConfigContent()

    @possibleException
    def put(self, pluginName):
        args = PluginConfigResourceParser.parsePostParameters()
        PluginConfigReader(pluginName).setConfigContent(args)
