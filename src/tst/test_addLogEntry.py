import unittest
import sys
sys.path.append('../')
from db_model import addLogEntry, getDbObject, getClientObject
from config_reader import getDbName

client = getClientObject()

# DB
TEST_DB = 'test_db'
TEST_DB_MASTER = getDbName()

# VALUES
TEST_USER_ID = 'test_user_id'
TEST_MSG = 'test_msg'
TEST_SERVICE = 'service'

# COLLECTIONS
LOG = 'log'

# FIELDS
TEST_USER_ID_FIELD = 'user_id'
TEST_MSG_FIELD = 'message'
TEST_SERVICE_FIELD = 'service'

db = getDbObject(TEST_DB)
db_master = getDbObject(TEST_DB_MASTER)


class TestAddLogEntry(unittest.TestCase):

    def testAddLogEntry(self):
        client.drop_database(TEST_DB)
        addLogEntry(TEST_DB, TEST_USER_ID, TEST_MSG)
        obj = db[LOG].find_one()
        self.assertEqual(obj[TEST_MSG_FIELD], TEST_MSG)
        self.assertEqual(obj[TEST_USER_ID_FIELD], TEST_USER_ID)
        self.assertTrue(TEST_SERVICE_FIELD not in obj)
        client.drop_database(TEST_DB)
        addLogEntry(TEST_DB_MASTER, TEST_USER_ID, TEST_MSG, TEST_SERVICE)
        objects = list(db_master[LOG].find({TEST_USER_ID_FIELD: TEST_USER_ID}))
        self.assertEqual(len(objects), 1)
        obj = objects[0]
        self.assertEqual(obj[TEST_MSG_FIELD], TEST_MSG)
        self.assertTrue(TEST_SERVICE_FIELD in obj)
        self.assertEqual(obj[TEST_SERVICE_FIELD], TEST_SERVICE)
