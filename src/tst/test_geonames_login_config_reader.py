import unittest
from config_reader import getGeonamesLogin

BEFORE_READ_VALUE = 'test'


class TestGeonamesLoginConfigReader(unittest.TestCase):

    def testGeonamesLoginConfigReader(self):
        geonamesLogin = getGeonamesLogin()
        self.assertTrue(len(geonamesLogin) != 0)
        self.assertNotEqual(BEFORE_READ_VALUE, geonamesLogin)
