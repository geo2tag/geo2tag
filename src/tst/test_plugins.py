import unittest
import sys
sys.path.append('../')
from db_model import getDbObject
from main import app
from plugins import isPluginEnabled

TEST_PLUGIN_NAME = 'test_plugin'


class TestPlugins(unittest.TestCase):
    def testIsPluginEnabled(self):
        print '-------------------------API'
        isPluginEnabled(TEST_PLUGIN_NAME, app)
        
