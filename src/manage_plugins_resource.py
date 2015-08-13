from flask_restful import reqparse
from flask.ext.restful import Resource
from possible_exception import possibleException
from flask import request
from db_model import setPluginState
from plugin_routines import isPluginEnabled, enablePlugin


class ManagePluginsResource(Resource):

    @possibleException
    def get(self):
        from main import app, getApi
        pluginsDict = dict((key, request.args.get(key))
                           for key in request.args.keys())

        for plugin in pluginsDict:
            setPluginState(plugin, pluginsDict[plugin])
            if pluginsDict[plugin].lower() == u'true' and isPluginEnabled(
                    plugin, app) == False:
                enablePlugin(getApi(), plugin)
