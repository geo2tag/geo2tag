import unittest
from plugin_config_reader import PluginConfigReader


TEST_CONTENT = {
    u'main': {
        u'db_name': u'test', u'port': u'111'}, u'geo': {
            u'geoname': u'g'}}

TEST_NAME = 'test'


class TestPluginConfigReader(unittest.TestCase):

    def testPluginConfigReader(self):
        pluginConfigReader = PluginConfigReader(TEST_NAME)
        conf = pluginConfigReader.getConfigContent()
        print conf
        pluginConfigReader.setConfigContent(TEST_CONTENT)
