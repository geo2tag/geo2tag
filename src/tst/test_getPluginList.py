import unittest
import os
from plugin_routines import getPluginList


class TestGetPluginList(unittest.TestCase):

    def testGetPluginList(self):
        print 'Before testGetPluginList {0}'.format(os.getcwd())
        os.chdir('../')
        pluginsList = getPluginList()
        _, dirs, _ = os.walk('plugins').next()
        os.chdir('tst/')
        self.assertEquals(dirs, pluginsList)
