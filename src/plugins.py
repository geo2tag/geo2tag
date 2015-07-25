#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join as joinpath
sys.path.append('plugins')

def getPluginList():
    pluginsDirList = os.listdir('plugins')
    pluginsList = []
    for i in pluginsDirList:
        if os.path.isdir(joinpath('plugins',i)):
            pluginsList.append(i)
    return pluginsList

def getPluginState(pluginName):
	return True