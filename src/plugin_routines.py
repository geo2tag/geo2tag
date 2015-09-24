#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join as joinpath
from traceback import format_exc
import imp
from url_routines import getPluginUrl
from log import writeInstanceLog
from user_routines import getUserId

PLUGINS_DIR_NAME = 'plugins'
# sys.path.append(PLUGINS_DIR_NAME)

GET_PLUGIN_RESOURCES = 'getPluginResources'
EXCEPT_ERROR_TEXT = 'Error occurred while loading the plugin '
ERROR_DISR_TEXT = 'error description: '
LOG_USERID = 'system'
PREFIX_LOAD_MAIN = 'plugins.'
LOAD_MAIN_ENDING = '.main'


def getPluginList():
    pluginsDirList = os.listdir(PLUGINS_DIR_NAME)
    pluginsList = []
    for i in pluginsDirList:
        if os.path.isdir(joinpath(PLUGINS_DIR_NAME, i)):
            pluginsList.append(i)
    return pluginsList


def enablePlugin(api, pluginName):
    loadMain = PREFIX_LOAD_MAIN + pluginName + LOAD_MAIN_ENDING
    try:
        loadModule = __import__(loadMain, globals(), locals(), [
                                GET_PLUGIN_RESOURCES], -1)
        pluginResourcesDict = loadModule.getPluginResources()
        for pluginResource in pluginResourcesDict:
            api.add_resource(pluginResourcesDict[pluginResource], getPluginUrl(
                pluginResource, pluginName))
        print(getUserId(), 'Plugin ' +
                         pluginName + ' successfully loaded')
    except Exception as e:
        writeInstanceLog(getUserId(), EXCEPT_ERROR_TEXT +
                         pluginName +
                         ', ' +
                         ERROR_DISR_TEXT +
                         str(e) +
                         ' ' +
                         str(format_exc()))


def isPluginEnabled(pluginName, app):
    url_map = getattr(app, 'url_map')
    for rule in url_map.iter_rules():
        if str(rule).find('/' + pluginName + '/') != -1:
            return True
    return False
