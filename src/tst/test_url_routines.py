import unittest
import sys
sys.path.append('../')
from url_routines import *

TEST_URL = 'test_url'
TEST_PLUGIN = 'test_plugin'
VALID_RESULT = '/instance/plugins/test_plugin/test_url'

class TestUrlRoutines(unittest.TestCase):
    def testUrlRoutines(self):
        RESULT = getPluginUrl(TEST_URL, TEST_PLUGIN)
        self.assertTrue(VALID_RESULT, RESULT)


