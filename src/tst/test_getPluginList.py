import unittest
import sys
import os
sys.path.append('../')
from plugins import getPluginList

TEST_PATH = os.getcwd()

class TestGetPluginList(unittest.TestCase):
    def testGetPluginList(self):
        os.chdir('../')
        pluginsList = getPluginList()
        root, dirs, files = os.walk('plugins').next()
        os.chdir(TEST_PATH)
        self.assertEquals(dirs, pluginsList)
