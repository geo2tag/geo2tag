import unittest
from db_model import addLogEntry, getDbObject, getClientObject
from config_reader import getDbName
from log import LOG_LVL_INFO

client = getClientObject()

# DB
TEST_DB = 'test_db'
TEST_DB_MASTER = getDbName()

# VALUES
TEST_USER_ID = 'test_user_id'
TEST_MSG = 'test_msg'
TEST_SERVICE = 'service'
TEST_LOG_LEVEL = LOG_LVL_INFO
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
        client.drop_database(TEST_DB)
        addLogEntry(TEST_DB, TEST_USER_ID, TEST_MSG, LOG_LVL_INFO)
        obj = db[LOG].find_one()
        self.assertEqual(obj[TEST_MSG_FIELD], TEST_MSG)
        self.assertEqual(obj[TEST_USER_ID_FIELD], TEST_USER_ID)
        self.assertEqual(obj[TEST_LEVEL_FIELD], TEST_LOG_LEVEL)
        self.assertTrue(TEST_SERVICE_FIELD not in obj)
        client.drop_database(TEST_DB)
        addLogEntry(
            TEST_DB_MASTER, 
            TEST_USER_ID,
            TEST_MSG,
            LOG_LVL_INFO, 
            TEST_SERVICE
        )
        objects = list(db_master[LOG].find({TEST_USER_ID_FIELD: TEST_USER_ID}))
        self.assertEqual(len(objects), 1)
        obj = objects[0]
        self.assertEqual(obj[TEST_MSG_FIELD], TEST_MSG)
        self.assertTrue(TEST_SERVICE_FIELD in obj)
        self.assertEqual(obj[TEST_SERVICE_FIELD], TEST_SERVICE)
        self.assertEqual(obj[TEST_LEVEL_FIELD], TEST_LOG_LEVEL)
