import unittest
import sys
import os
sys.path.append('../')
from plugins import getPluginList


class TestGetPluginList(unittest.TestCase):
    def testGetPluginList(self):
        os.chdir('../')
        pluginsList = getPluginList()
        root, dirs, files = os.walk('plugins').next()
        os.chdir('tst')
        self.assertEquals(dirs, pluginsList)