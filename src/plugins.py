#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


import imp
from flask import Flask
from flask.ext.restful import Api
app = Flask(__name__)
api = Api(app)

def __import__(module):
	f, filename, description = imp.find_module('plugins')
	return imp.load_module(module, f, filename, description)

def enablePlugin(api, pluginName):
	print __import__('getPluginResources')

if __name__ == '__main__':
	enablePlugin(api, 'testPlugin1')