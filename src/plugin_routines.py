#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join as joinpath

PLUGINS_DIR_NAME = 'plugins'
sys.path.append(PLUGINS_DIR_NAME)

import imp
from url_routines import getPluginUrl

GET_PLUGIN_RESOURCES = 'getPluginResources'
EXCEPT_ERROR_TEXT = 'Error occurred while loading the plugin '
PREFIX_LOAD_MAIN = 'plugins.'
LOAD_MAIN_ENDING = '.main'

def getPluginList():
    pluginsDirList = os.listdir(PLUGINS_DIR_NAME)
    pluginsList = []
    for i in pluginsDirList:
        if os.path.isdir(joinpath(PLUGINS_DIR_NAME,i)):
            pluginsList.append(i)
    return pluginsList

def enablePlugin(api, pluginName):
    loadMain = PREFIX_LOAD_MAIN + pluginName + LOAD_MAIN_ENDING
    loadModule = __import__ (loadMain, globals(), locals(), [GET_PLUGIN_RESOURCES], -1)
    try:
        pluginResourcesDict = loadModule.getPluginResources()
        for pluginResource in pluginResourcesDict:
            print getPluginUrl(pluginResource, pluginName)
            api.add_resource(pluginResourcesDict[pluginResource], getPluginUrl(pluginResource, pluginName))
    except Exception as e:
        print EXCEPT_ERROR_TEXT + pluginName
        print e

def isPluginEnabled(pluginName, app):
    url_map = getattr(app, 'url_map')
    for rule in url_map.iter_rules():
        if str(rule).find('/' + pluginName + '/') != -1:
            return True
    return False
