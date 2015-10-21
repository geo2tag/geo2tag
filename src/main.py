# -*- coding: utf-8 -*-
from manage_plugins_resource import ManagePluginsResource
from tests_resource import TestsResource
from point_resource import PointResource
from flask import Flask
from flask.ext.restful import Api
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
from login_facebook_resource import LoginFacebookResource, facebook_oauth
from db_model import closeConnection, getPluginState
import atexit
from plugin_routines import getPluginList, enablePlugin
from map_resource import MapResource
from plugin_list_resource import GetAllPluginsWithStatusResource
from user_routines import getUserId
from flask import request
from log import writeInstanceLog
from config_reader import getInstancePrefix
from flask import g
from possible_exception import possibleException
from flask import request
from url_routines import isPluginUrl
from plugin_not_enabled_exception import PluginNotEnabledException
from log import writeInstanceLog
from user_routines import getUserId
from internal_tests_resource import InternalTestsResource
from log import writeInstanceLog
from user_routines import getUserId
from admin_log_resource import AdminLogResource
from admin_service_list_resource import AdminServiceListResource
API = None


def output_json(obj, code, headers=None):
    if isinstance(obj, str) == True:
        return make_response(obj, code, headers)
    return make_response(json_util.dumps(obj), code, headers)


def getApi():
    global API
    if API is None:
        API = Api(app)
    return API

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
app = Flask(__name__)
app.register_blueprint(google_oauth)
app.register_blueprint(facebook_oauth)

app.secret_key = urandom(32)
getApi().representations = DEFAULT_REPRESENTATIONS


@app.after_request
def after_request(response):
    writeInstanceLog(getUserId(), 'Request url: ' + request.url +
                                  ', request data: ' + request.data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
    writeInstanceLog(getUserId(),
                     'Status_code: ' + str(response.status_code) + ', '
                     'response: ' + str(response.response)[:2000])
    return response


@app.before_request
def defineInstancePrefix():
    g.instance_prefix = getInstancePrefix()

getApi().add_resource(ServiceResource,
                      getPathWithPrefix('/service/<string:serviceName>'))
getApi().add_resource(StatusResource, getPathWithPrefix('/status'))
getApi().add_resource(ServiceListResource, getPathWithPrefix('/service'))
getApi().add_resource(DebugInfoResource, getPathWithPrefix('/debug_info'))
getApi().add_resource(
    LogResource,
    getPathWithPrefix('/service/<string:serviceName>/log'),
    getPathWithPrefix('/log'))


@app.before_request
@possibleException
def before_request():
    if isPluginUrl(request.url):
        pluginUrlList = request.url.split('/')
        pluginNameIndex = pluginUrlList.index('plugin') + 1
        if getPluginState(pluginUrlList[pluginNameIndex]) == False:
            raise PluginNotEnabledException

getApi().add_resource(ChannelsListResource, getPathWithPrefix(
    '/service/<string:serviceName>/channel'))
getApi().add_resource(ChannelResource, getPathWithPrefix(
    '/service/<string:serviceName>/channel/<string:channelId>'))

getApi().add_resource(PointResource, getPathWithPrefix(
    '/service/<string:serviceName>/point/<string:pointId>'))
getApi().add_resource(PointListResource, getPathWithPrefix(
    '/service/<string:serviceName>/point'))


getApi().add_resource(LogoutResource, getPathWithPrefix('/logout'))
getApi().add_resource(LoginResource, getPathWithPrefix('/login'))
getApi().add_resource(LoginGoogleResource, getPathWithPrefix('/login/google'))
getApi().add_resource(LoginFacebookResource,
                      getPathWithPrefix('/login/facebook'))
getApi().add_resource(DebugLoginResource, getPathWithPrefix('/login/debug'))
getApi().add_resource(TestsResource, getPathWithPrefix('/tests'))
getApi().add_resource(AdminServiceListResource, getPathWithPrefix(
    '/admin/service'))

getApi().add_resource(
    MapResource,
    getPathWithPrefix('/service/<string:serviceName>/map'))
getApi().add_resource(
    GetAllPluginsWithStatusResource,
    getPathWithPrefix('/plugin'))
getApi().add_resource(
    ManagePluginsResource,
    getPathWithPrefix('/manage_plugins'))
getApi().add_resource(
    InternalTestsResource,
    getPathWithPrefix('/internal_tests'))
getApi().add_resource(
    AdminLogResource,
    getPathWithPrefix('/admin/log'))


def initApp(api):
    import os
    homeDir = os.getcwd()
    if homeDir.find('/var/www') != -1:
        homeDir = '/var/www/geomongo/'
        os.chdir(homeDir)
    else:
        if homeDir.find('src/tst') != -1:
            os.chdir('..')
    pluginList = getPluginList()
    for pluginName in pluginList:
        if getPluginState(pluginName) is True:
            enablePlugin(api, pluginName)
    os.chdir(homeDir)

atexit.register(closeConnection)

initApp(getApi())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
