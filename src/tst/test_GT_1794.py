import unittest
from plugin_routines import addConfigurablePlugin, \
    existConfigPlugin, \
    checkConfigPlugin
import os


class TestConfigPlugin(unittest.TestCase):

    def testAddConfigurablePlugin(self):
        self.assertTrue(addConfigurablePlugin("testPlugin1", True))
        self.assertFalse(addConfigurablePlugin("testPlugin", False))

    def testExistConfigPlugin(self):
        os.chdir('../')
        self.assertTrue(existConfigPlugin("testPlugin1"), True)
        self.assertFalse(existConfigPlugin("testPlugin2"))
        os.chdir('tst')

    def testCheckConfigPlugin(self):
        os.chdir('../')
        self.assertTrue(checkConfigPlugin("testPlugin1"), True)
        self.assertFalse(checkConfigPlugin("testPlugin2"), False)
        os.chdir('tst')
