from flask_restful import reqparse
from flask.ext.restful import Resource
from possible_exception import possibleException
from flask import request
from db_model import setPluginState
from __import__ import isPluginEnabled, enablePlugin

'''def pluginsDictRequest(pluginsList):
    pluginDict = {}
    for plugin in pluginsList:
        somePlugin = []
        somePlugin.append(plugin[0])
        print plugin, somePlugin
        if plugin[1].lower() == 'true':
            somePlugin.append(True)
            print somePlugin
        elif plugin[1].lower() == 'false':
            somePlugin.append(False)
            print somePlugin
        else:
            continue
        pluginDict[somePlugin[0]] = somePlugin[1]
    return pluginDict'''

class ManagePluginsResource(Resource):
    @possibleException
    def get(self):
        from main import api
        pluginsList = dict((key, request.args.getlist(key)) for key in request.args.keys())
        for plugin in pluginsList:
            setPluginState(plugin, pluginsList[plugin])
            if pluginsList[plugin].lower() == u'true' and isPluginEnabled(plugin, api) == False:
                enablePlugin(plugin, api)