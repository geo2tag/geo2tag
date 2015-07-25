import unittest
import sys
import os
sys.path.append('../')
from plugins import getPluginList


class TestGetPluginList(unittest.TestCase):
    def testGetPluginList(self):
        os.chdir('../')
        print '333333', os.getcwd()
        pluginsList = getPluginList()
        print '44444444', os.getcwd()
        root, dirs, files = os.walk('plugins').next()
        os.chdir('tst')
        self.assertEquals(dirs, pluginsList)