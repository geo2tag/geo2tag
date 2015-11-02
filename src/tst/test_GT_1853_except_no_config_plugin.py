from unittest import TestCase
from plugin_not_configurable import PluginIsNotConfigurable
from plugin_config_reader import PluginConfigReader
from plugin_routines import checkConfigPlugin

TEST_PLUG = 'noplugasdfg'


class TestExcetPluginNotConfig(TestCase):

    def testExcetPluginNotConfig_check(self):
        with self.assertRaises(PluginIsNotConfigurable):
            checkConfigPlugin(TEST_PLUG)

    def testExcetPluginNotConfig_raise(self):
        with self.assertRaises(PluginIsNotConfigurable):
            raise PluginIsNotConfigurable()
