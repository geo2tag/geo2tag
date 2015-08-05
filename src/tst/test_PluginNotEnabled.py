import unittest
import sys
sys.path.append('../')
from plugin_not_enabled_exception import PluginNotEnabledException

class TestPluginNotEnabledException(unittest.TestCase):
    def testPluginNotEnabledException(self):
        with self.assertRaises(PluginNotEnabledException) as e:
            raise PluginNotEnabledException()