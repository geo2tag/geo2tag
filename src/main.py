# -*- coding: utf-8 -*-
from tests_resource import TestsResource
from point_resource import PointResource
from flask import Flask, current_app
from flask.ext.restful import Resource, Api
from service_resource import ServiceResource
from service_list_resource import ServiceListResource
from status_resource import StatusResource
from log_resource import LogResource
from debug_info_resource import DebugInfoResource
from flask import make_response
from bson import json_util
from channels_list_resource import ChannelsListResource
from channel_resource import ChannelResource
from point_list_resource import PointListResource
from os import urandom
from logout_resource import LogoutResource
from login_resource import LoginResource
from url_utils import getPathWithPrefix
from debug_login_resource import DebugLoginResource
from login_google_resource import LoginGoogleResource, google_oauth
from db_model import closeConnection
import atexit
from plugins import getPluginList, getPluginState, enablePlugin
from os.path import join as joinpath
from plugin_list_resource import GetAllPluginsWithStatusResource


API = None

def output_json(obj, code, headers=None):
    if isinstance(obj, str) == True:
        return make_response(obj, code)
    return make_response(json_util.dumps(obj), code)

def getApi():
    global API
    if API == None:
        API = Api(app)
    return API

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
app = Flask(__name__)
app.register_blueprint(google_oauth)

app.secret_key = urandom(32)
getApi().representations = DEFAULT_REPRESENTATIONS

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    return response

getApi().add_resource(ServiceResource, getPathWithPrefix('/service/<string:serviceName>'))
getApi().add_resource(StatusResource, getPathWithPrefix('/status'))
getApi().add_resource(ServiceListResource, getPathWithPrefix('/service'))
getApi().add_resource(DebugInfoResource, getPathWithPrefix('/debug_info'))
getApi().add_resource(LogResource, getPathWithPrefix('/service/<string:serviceName>/log'),
                              getPathWithPrefix('/log'))
getApi().add_resource(ChannelsListResource, getPathWithPrefix('/service/<string:serviceName>/channel'))
getApi().add_resource(ChannelResource, getPathWithPrefix('/service/<string:serviceName>/channel/<string:channelId>'))

getApi().add_resource(PointResource, getPathWithPrefix('/service/<string:serviceName>/point/<string:pointId>'))
getApi().add_resource(PointListResource, getPathWithPrefix('/service/<string:serviceName>/point'))

getApi().add_resource(LogoutResource, getPathWithPrefix('/logout'))
getApi().add_resource(LoginResource, getPathWithPrefix('/login'))
getApi().add_resource(LoginGoogleResource, getPathWithPrefix('/login/google'))
getApi().add_resource(DebugLoginResource, getPathWithPrefix('/login/debug'))
getApi().add_resource(TestsResource, getPathWithPrefix('/tests'))
getApi().add_resource(GetAllPluginsWithStatusResource, getPathWithPrefix('/plugin'))

def initApp(api):
    import os
    homeDir = os.getcwd()
    if os.getcwd().find('/var/www') != -1:
        homeDir = '/var/www/geomongo/'
        os.chdir(homeDir)        
    else:
        if os.getcwd().find('src/tst') != -1:
            os.chdir('..')
    homeDir = os.getcwd()
    pluginList = getPluginList()
    for pluginName in pluginList:
        if getPluginState(pluginName) is True:
            os.chdir(homeDir)
            enablePlugin(api, pluginName)
    os.chdir(homeDir)

atexit.register(closeConnection)

initApp(getApi())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

