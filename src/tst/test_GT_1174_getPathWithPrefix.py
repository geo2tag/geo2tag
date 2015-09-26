from unittest import TestCase
from url_utils import getPathWithPrefix

TEST_PATH = '/instance/status'
TEST_STR = '/status'


class GetPathWithPrefixTest(TestCase):

    def testGetPathWithPrefix(self):
        RESULT_PATH = getPathWithPrefix('/status')
        self.assertEqual(RESULT_PATH, TEST_PATH)
