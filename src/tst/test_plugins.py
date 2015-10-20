import unittest
import os
from main import app
from plugin_routines import isPluginEnabled, enablePlugin
from flask import Flask
from flask_restful import Api

TEST_PLUGIN_NAME = 'test_plugin'
TEST_PLUGIN_NAME_NOT_VALID = 'test_plugin_not_valid_name'
TEST_PATH = os.getcwd()

app = Flask(__name__)
api = Api(app)


class TestPlugins(unittest.TestCase):

    def testIsPluginEnabled(self):
        os.chdir('../')
        enablePlugin(api, TEST_PLUGIN_NAME)
        os.chdir(TEST_PATH)
        RESULT = isPluginEnabled(TEST_PLUGIN_NAME, app)
        self.assertTrue(RESULT is True)
        RESULT = isPluginEnabled(TEST_PLUGIN_NAME_NOT_VALID, app)
        self.assertTrue(RESULT is False)
