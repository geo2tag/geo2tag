# -*- coding: utf-8 -*-
from setuptools.command.egg_info import write_pkg_info
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
from plugin_routines import getPluginList, getPluginState, enablePlugin
from os.path import join as joinpath
from plugin_list_resource import GetAllPluginsWithStatusResource
from user_routines import getUserId
from flask import request
from log import writeInstanceLog

def output_json(obj, code, headers=None):
    if isinstance(obj, str) == True:
        return make_response(obj, code)
    return make_response(json_util.dumps(obj), code)

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
app = Flask(__name__)
app.register_blueprint(google_oauth)

app.secret_key = urandom(32)
api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS


@app.after_request
def after_request(response):
    writeInstanceLog(getUserId(), 'Request path: ' + request.url + ', request data: ' + request.data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    return response

api.add_resource(ServiceResource, getPathWithPrefix('/service/<string:serviceName>'))
api.add_resource(StatusResource, getPathWithPrefix('/status'))
api.add_resource(ServiceListResource, getPathWithPrefix('/service'))
api.add_resource(DebugInfoResource, getPathWithPrefix('/debug_info'))
api.add_resource(LogResource, getPathWithPrefix('/service/<string:serviceName>/log'),
                              getPathWithPrefix('/log'))
api.add_resource(ChannelsListResource, getPathWithPrefix('/service/<string:serviceName>/channel'))
api.add_resource(ChannelResource, getPathWithPrefix('/service/<string:serviceName>/channel/<string:channelId>'))

api.add_resource(PointResource, getPathWithPrefix('/service/<string:serviceName>/point/<string:pointId>'))
api.add_resource(PointListResource, getPathWithPrefix('/service/<string:serviceName>/point'))

api.add_resource(LogoutResource, getPathWithPrefix('/logout'))
api.add_resource(LoginResource, getPathWithPrefix('/login'))
api.add_resource(LoginGoogleResource, getPathWithPrefix('/login/google'))
api.add_resource(DebugLoginResource, getPathWithPrefix('/login/debug'))
api.add_resource(TestsResource, getPathWithPrefix('/tests'))
api.add_resource(GetAllPluginsWithStatusResource, getPathWithPrefix('/plugin'))


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

initApp(api)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

