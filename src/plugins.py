#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


import imp
from main import api
from os.path import join as pathjoin
from url_routines import getPluginUrl

def enablePlugin(api, pluginName):
    dirName = 'plugins/' + pluginName
    os.chdir(dirName)
    fileName = pathjoin(os.getcwd(), 'main.py')
    module = imp.load_source('getPluginResources',  fileName)
    pluginResourcesList = module.getPluginResources()
    for pluginResource in pluginResourcesList:
        api.add_resource(pluginResource.values()[0], getPluginUrl(pluginResource.keys()[0], pluginName))