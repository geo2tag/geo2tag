#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join as joinpath
sys.path.append('plugins')
import imp
from url_routines import getPluginUrl

def getPluginList():
    pluginsDirList = os.listdir('plugins')
    pluginsList = []
    for i in pluginsDirList:
        if os.path.isdir(joinpath('plugins',i)):
            pluginsList.append(i)
    return pluginsList

def enablePlugin(api, pluginName):
    dirName = 'plugins/' + pluginName
    os.chdir(dirName)
    fileName = joinpath(os.getcwd(), 'main.py')
    module = imp.load_source('getPluginResources',  fileName)
    pluginResourcesList = module.getPluginResources()
    for pluginResource in pluginResourcesList:
        api.add_resource(pluginResource.values()[0], getPluginUrl(pluginResource.keys()[0], pluginName))

def getPluginState(pluginName):
    return True