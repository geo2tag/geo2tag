#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join as joinpath
from werkzeug.routing import BaseConverter

PLUGINS_DIR_NAME = 'plugins'
sys.path.append(PLUGINS_DIR_NAME)

import imp
from url_routines import getPluginUrl

CONCAT_PLUGIN_DIR = 'plugins/'
MAIN_FILE = 'main.py'
GET_PLUGIN_RESOURCES = 'getPluginResources'
EXCEPT_ERROR_TEXT = 'Error occurred while loading the plugin '

class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split(',')
    def to_url(self, values):
        return ','.join(BaseConverter.to_url(value)
                        for value in values)

def getPluginList():
    pluginsDirList = os.listdir(PLUGINS_DIR_NAME)
    pluginsList = []
    for i in pluginsDirList:
        if os.path.isdir(joinpath(PLUGINS_DIR_NAME,i)):
            pluginsList.append(i)
    return pluginsList

def enablePlugin(api, pluginName):
    dirName = CONCAT_PLUGIN_DIR + pluginName
    os.chdir(dirName)
    fileName = joinpath(os.getcwd(), MAIN_FILE)
    sys.path.append('../../' + dirName)
    try:
        module = imp.load_source(GET_PLUGIN_RESOURCES,  fileName)
        pluginResourcesDict = module.getPluginResources()
        for pluginResource in pluginResourcesDict:
            print getPluginUrl(pluginResource, pluginName)
            api.add_resource(pluginResourcesDict[pluginResource], getPluginUrl(pluginResource, pluginName))
    except Exception as e:
        print EXCEPT_ERROR_TEXT + pluginName
        print e

def getPluginState(pluginName):
    return True

def isPluginEnabled(pluginName, app):
    url_map = getattr(app, 'url_map')
    for rule in url_map.iter_rules():
        if str(rule).find('/' + pluginName + '/') != -1:
            return True
    return False
