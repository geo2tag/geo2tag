from flask_restful import reqparse
from flask.ext.restful import Resource
from possible_exception import possibleException
from flask import request
from db_model import setPluginState
from plugin_routines import isPluginEnabled, enablePlugin

class ManagePluginsResource(Resource):
    @possibleException
    def get(self):
        from main import app, api
        pluginsList = dict((key, request.args.get(key)) for key in request.args.keys())
        for plugin in pluginsList:
            setPluginState(plugin, pluginsList[plugin])
            if pluginsList[plugin].lower() == u'true' and isPluginEnabled(plugin, app) == False:
                enablePlugin(api, plugin)