import unittest
import sys
from pymongo import MongoClient

sys.path.append('../')
from config_reader import getDebugUsers
TEST_VALID_RESULT = ['debug_user1','debug_user2','debug_user3']

class TestConfigReader(unittest.TestCase):
    def testGetDebugUsers(self):
        RESULT = getDebugUsers()
        self.assertEqual(TEST_VALID_RESULT, RESULT)
