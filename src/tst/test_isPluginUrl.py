from unittest import TestCase
from url_routines import isPluginUrl
URL = 'http://geomongo/instance/plugin/test_plugin/res1'
BAD_URL = 'http://geomongo/instance/my_plugin'


class TestIsPluginUrl(TestCase):

    def testIsPluginUrl(self):
        self.assertTrue(isPluginUrl(URL))
        self.assertFalse(isPluginUrl(BAD_URL))
