from possible_exception import possibleException
from flask_restful import Resource
from plugin_config_resource_parser import PluginConfigResourceParser
from plugin_config_reader import PluginConfigReader
from plugin_routines import checkConfigPlugin
from plugin_not_configurable import PluginIsNotConfigurable


class PluginConfigResource(Resource):

    @possibleException
    def get(self, pluginName):
        try:
            checkConfigPlugin(pluginName)
            return PluginConfigReader(pluginName).getConfigContent()
        except PluginIsNotConfigurable as e:
            return e.getReturnObject()

    @possibleException
    def put(self, pluginName):
        try:
            args = PluginConfigResourceParser.parsePostParameters()
            PluginConfigReader(pluginName).setConfigContent(args)
        except PluginIsNotConfigurable as e:
            return e.getReturnObject()
