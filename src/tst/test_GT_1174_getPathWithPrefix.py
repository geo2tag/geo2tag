from unittest import TestCase
import sys
sys.path.append('../')
from main import *

TEST_PATH = '/instance/status'
TEST_STR = '/status'

class GetPathWithPrefixTest(TestCase):
    def testGetPathWithPrefix(self):
        RESULT_PATH = getPathWithPrefix('/status')
        self.assertEqual(RESULT_PATH, TEST_PATH)
