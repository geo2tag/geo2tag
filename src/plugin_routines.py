#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join as joinpath
from traceback import format_exc
from url_routines import getPluginUrl
from log import writeInstanceLog
from log import LOG_LVL_INFO
from log import LOG_LVL_ERROR
from user_routines import getUserId
from db_model import getDbObject
PLUGINS_DIR_NAME = 'plugins'

GET_PLUGIN_RESOURCES = 'getPluginResources'
EXCEPT_ERROR_TEXT = 'Error occurred while loading the plugin '
ERROR_DISR_TEXT = 'error description: '
LOG_USERID = 'system'
PREFIX_LOAD_MAIN = 'plugins.'
LOAD_MAIN_ENDING = '.main'
CONFIG = "config.ini"
PLUGINS = "plugins"
CONFIGURABLE = "configurable"


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
        writeInstanceLog(getUserId(), 'Plugin ' +
                         pluginName + ' successfully loaded',
                         LOG_LVL_INFO)
    except Exception as e:
        writeInstanceLog(getUserId(), EXCEPT_ERROR_TEXT +
                         pluginName +
                         ', ' +
                         ERROR_DISR_TEXT +
                         str(e) +
                         ' ' +
                         str(format_exc()),
                         LOG_LVL_ERROR)


def isPluginEnabled(pluginName, app):
    url_map = getattr(app, 'url_map')
    for rule in url_map.iter_rules():
        if str(rule).find('/' + pluginName + '/') != -1:
            return True
    return False


def addConfigurablePlugin(pluginName, existConfig):
    collection = getDbObject()[PLUGINS]
    obj = collection.find_one({"name": pluginName})
    if obj is None:
        return False
    if existConfig:
        obj[CONFIGURABLE] = True
    else:
        obj[CONFIGURABLE] = False
    collection.save(obj)
    return True


def existConfigPlugin(pluginName):
    existConfig = CONFIG in os.listdir(PLUGINS_DIR_NAME + "/" + pluginName)
    if not(existConfig):
        return False
    if addConfigurablePlugin(pluginName, existConfig):
        return True


def checkConfigPlugin(pluginName):
    if existConfigPlugin(pluginName):
        return True
    return False
