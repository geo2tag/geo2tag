from flask import request
from flask.ext.restful import Resource
from plugins import getPluginList, getPluginState

class GetAllPluginsWithStatusResource(Resource):
    def get(self):
        list_plugins = getPluginList()
        result = {}
        for plugin in list_plugins:
            result.update({plugin:getPluginState(plugin)})
        return result
