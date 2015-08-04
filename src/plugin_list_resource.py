from flask import request
from flask.ext.restful import Resource
from plugin_routines import getPluginList
from db_model import getPluginState

class GetAllPluginsWithStatusResource(Resource):
    def get(self):
        list_plugins = getPluginList()
        result = {}
        for plugin in list_plugins:
            result.update({plugin:getPluginState(plugin)})
        return result
