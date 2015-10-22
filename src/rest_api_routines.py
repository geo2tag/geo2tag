import os
from bson import json_util
from os import urandom
from login_google_resource import google_oauth
from login_facebook_resource import facebook_oauth
from flask import make_response, request, g, Flask
from db_model import getPluginState
from possible_exception import possibleException
from plugin_routines import getPluginList, enablePlugin
from config_reader import getInstancePrefix
from flask_restful import Api
from url_routines import isPluginUrl
from plugin_not_enabled_exception import PluginNotEnabledException
from log import writeInstanceLog
from user_routines import getUserId
from config_reader import getInstancePrefix

API = None
app = Flask(__name__)
app.register_blueprint(google_oauth)
app.register_blueprint(facebook_oauth)
app.secret_key = urandom(32)

def output_json(obj, code, headers=None):
    if isinstance(obj, str) == True:
        return make_response(obj, code, headers)
    return make_response(json_util.dumps(obj), code, headers)

DEFAULT_REPRESENTATIONS = {'application/json': output_json}

def getApi():
    global API
    if API is None:
        API = Api(app)
    return API

def getApp():
    global app
    return app    

def initApp(api):
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


@app.before_request
@possibleException
def before_request():
    if isPluginUrl(request.url):
        pluginUrlList = request.url.split('/')
        pluginNameIndex = pluginUrlList.index('plugin') + 1
        if getPluginState(pluginUrlList[pluginNameIndex]) == False:
            raise PluginNotEnabledException


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

