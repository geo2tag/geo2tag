import unittest
import sys
import os
sys.path.append('../')
from plugin_routines import getPluginList


class TestGetPluginList(unittest.TestCase):
    def testGetPluginList(self):
        print 'testGetPluginList'
        print  os.getcwd()        
        os.chdir('../')
        pluginsList = getPluginList()
        root, dirs, files = os.walk('plugins').next()
        os.chdir('tst')
        self.assertEquals(dirs, pluginsList)
