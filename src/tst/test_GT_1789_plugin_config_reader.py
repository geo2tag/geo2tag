from unittest import TestCase
import plugin_config_reader


class TestPluginConfigReader(TestCase):
    def getConfigContent(self):
        print "getConfigContent"
        conf = PluginConfigReader.getConfigContent()
