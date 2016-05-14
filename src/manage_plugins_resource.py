from flask_restful import Resource
from possible_exception import possibleException
from flask import request
from db_model import setPluginState
from plugin_routines import isPluginEnabled, enablePlugin
from plugin_does_not_exist_exception import PluginDoesNotExistException
from rest_api_routines import getApi, getApp
import os


class ManagePluginsResource(Resource):

    @possibleException
    def get(self):
        pluginsDict = dict((key, request.args.get(key))
                           for key in request.args.keys())
        for plugin in pluginsDict:
            setPluginState(plugin, pluginsDict[plugin])
            if pluginsDict[plugin].lower() == u'true' and isPluginEnabled(
                    plugin, getApp()) == False:
                dirs = os.walk("plugins").next()
                if plugin not in dirs[1]:
                    raise PluginDoesNotExistException(plugin)
                else:
                    enablePlugin(getApi(), plugin)
