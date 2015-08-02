#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join as joinpath
PLUGINS_DIR_NAME = 'plugins'
sys.path.append(PLUGINS_DIR_NAME)

import imp
from url_routines import getPluginUrl
from log import writeInstanceLog

CONCAT_PLUGIN_DIR = 'plugins/'
MAIN_FILE = 'main.py'
GET_PLUGIN_RESOURCES = 'getPluginResources'
EXCEPT_ERROR_TEXT = 'Error occurred while loading the plugin '
ERROR_DISR_TEXT = 'error description: '
LOG_USERID = 'system'

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
        module = imp.load_source(GET_PLUGIN_RESOURCES, fileName)
        pluginResourcesDict = module.getPluginResources()
        for pluginResource in pluginResourcesDict:
            print getPluginUrl(pluginResource, pluginName)
            api.add_resource(pluginResourcesDict[pluginResource], getPluginUrl(pluginResource, pluginName))
        writeInstanceLog(LOG_USERID, 'Plugin ' + pluginName + ' successfully loaded')
    except Exception as e:
        writeInstanceLog(LOG_USERID, EXCEPT_ERROR_TEXT + pluginName + ', ' + ERROR_DISR_TEXT + str(e))

def getPluginState(pluginName):
    return True
