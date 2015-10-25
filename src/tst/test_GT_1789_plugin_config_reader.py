import unittest
from plugin_config_reader import PluginConfigReader


TEST_CONTENT = {u'main': {u'db_name': u'test', u'port': u'111'}, u'geo': {u'geoname': u'g'}}

class TestPluginConfigReader(unittest.TestCase):
    def testPluginConfigReader(self):
        print "getConfigContent-------"
        pluginConfigReader = PluginConfigReader('test')
        conf = pluginConfigReader.getConfigContent()
        pluginConfigReader.setConfigContent(TEST_CONTENT)
