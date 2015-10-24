import unittest
import pymongo
from db_model import addLogEntry, getDbObject, getClientObject
from config_reader import getDbName
from log import LOG_LVL_INFO
from log import LOG_LVL_CRITICAL

client = getClientObject()

# DB
TEST_DB = 'testservice'
TEST_DB_MASTER = getDbName()

# VALUES
TEST_USER_ID = 'test_user_id'
TEST_MSG = 'test_msg'
TEST_SERVICE = 'service'
TEST_LOG_LEVEL_INFO = LOG_LVL_INFO
TEST_LOG_LEVEL_CRITICAL = LOG_LVL_CRITICAL
# COLLECTIONS
LOG = 'log'

# FIELDS
TEST_USER_ID_FIELD = 'user_id'
TEST_MSG_FIELD = 'message'
TEST_SERVICE_FIELD = 'service'
TEST_LEVEL_FIELD = 'level'

db = getDbObject(TEST_DB)
db_master = getDbObject(TEST_DB_MASTER)


class TestAddLogEntry(unittest.TestCase):

    def testAddLogEntry(self):
        addLogEntry(TEST_DB, TEST_USER_ID, TEST_MSG, LOG_LVL_INFO)
        obj = list(db[LOG].find().sort('_id', pymongo.DESCENDING).limit(1))[0]
        self.assertEqual(obj[TEST_MSG_FIELD], TEST_MSG)
        self.assertEqual(obj[TEST_USER_ID_FIELD], TEST_USER_ID)
        self.assertEqual(obj[TEST_LEVEL_FIELD], TEST_LOG_LEVEL_INFO)
        self.assertTrue(TEST_SERVICE_FIELD not in obj)
        addLogEntry(
            TEST_DB_MASTER,
            TEST_USER_ID,
            TEST_MSG,
            TEST_LOG_LEVEL_CRITICAL,
            TEST_SERVICE
        )
        obj = list(db_master[LOG].find().sort('_id', pymongo.DESCENDING).limit(1))[0]
        self.assertEqual(obj[TEST_MSG_FIELD], TEST_MSG)
        self.assertTrue(TEST_SERVICE_FIELD in obj)
        self.assertEqual(obj[TEST_SERVICE_FIELD], TEST_SERVICE)
        self.assertEqual(obj[TEST_LEVEL_FIELD], TEST_LOG_LEVEL_CRITICAL)
