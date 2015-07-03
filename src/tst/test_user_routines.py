import unittest
import sys
from pymongo import MongoClient
from user_routines import logUserIn, logUserOut
sys.path.append('../')
from config_reader import getDbName

TEST_MASTER_DB = getDbName()
TEST_COLLECTION_LOG = 'log'
TEST_COLLECTION_SESSION = 'session'

TEST_MSG_LOGIN = 'login'
TEST_MSG_LOGOUT = 'logout'
TEST_ID = 'test_id'

TEST_USER_ID_FIELD = 'user_id'
TEST_MSG_FIELD = 'message'


client = MongoClient()
db = client[TEST_MASTER_DB]

class TestUserRoutines(unittest.TestCase):
    def testUserRoutines(self):
        logUserIn(TEST_ID)
        objects = list(db[TEST_COLLECTION_LOG].find({TEST_USER_ID_FIELD : TEST_ID}))
        self.assertEqual(len(objects), 1)
        obj = objects[0]
        self.assertEqual(obj[TEST_MSG_FIELD], TEST_MSG_LOGIN)
        db[TEST_COLLECTION_LOG].remove({TEST_USER_ID_FIELD : TEST_ID})
        objects = list(db[TEST_COLLECTION_SESSION].find({TEST_USER_ID_FIELD : TEST_ID}))
        self.assertEqual(len(objects), 1)
        logUserOut(TEST_ID)
        objects = list(db[TEST_COLLECTION_LOG].find({TEST_USER_ID_FIELD : TEST_ID}))
        self.assertEqual(len(objects), 1)
        obj = objects[0]
        self.assertEqual(obj[TEST_MSG_FIELD], TEST_MSG_LOGOUT)
        db[TEST_COLLECTION_LOG].remove({TEST_USER_ID_FIELD : TEST_ID})
        objects = list(db[TEST_COLLECTION_SESSION].find({TEST_USER_ID_FIELD : TEST_ID}))
        self.assertEqual(len(objects), 0)
        
