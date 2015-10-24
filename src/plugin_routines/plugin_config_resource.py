from possible_exception import possibleException
from flask_restful import Resource
from plugin_config_resource_parser import PluginConfigResourceParser
# from plugin_routines import checkConfigPlugin


class PluginConfigResource(Resource):

    @possibleException
    def get(self, pluginName):
        pass
        # if checkConfigPlugin(pluginName):
        # return PluginConfigReader().getConfigContent()
        # else:
        # return 'No plugin config'

    @possibleException
    def put(self, pluginName):
        # if checkConfigPlugin(pluginName):
        args = PluginConfigResourceParser.parsePostParameters()
        return args
        # PluginConfigReader().setConfigContent(postData)
        # else:
        # return 'No plugin config'
