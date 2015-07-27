#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join as joinpath
PLUGINS_DIR_NAME = 'plugins'
sys.path.append(PLUGINS_DIR_NAME)
import imp
from url_routines import getPluginUrl

CONCAT_PLUGIN_DIR = 'plugins/'
MAIN_FILE = 'main.py'
GET_PLUGIN_RESOURCES = 'getPluginResources'
EXCEPT_ERROR_TEXT = 'Error occurred while loading the plugin'

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
    try:
        module = imp.load_source(GET_PLUGIN_RESOURCES,  fileName)
        pluginResourcesList = module.getPluginResources()
        for pluginResource in pluginResourcesList:
            api.add_resource(pluginResource.values()[0], getPluginUrl(pluginResource.keys()[0], pluginName))
    except:
        print EXCEPT_ERROR_TEXT