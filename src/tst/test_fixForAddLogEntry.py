import unittest
from datetime import datetime
import sys

sys.path.append('../')
from db_model import addLogEntry, getDbObject
from config_reader import getDbName

# DB
TEST_DB = getDbName()

# VALUES
TEST_USER_ID = 'fix_test_user_id'
TEST_MSG = 'test_msg'
TEST_SERVICE = 'service'

# COLLECTIONS
LOG = 'log'

# Fields
DATE = 'date'

db = getDbObject()


class TestFixForAddLogEntry(unittest.TestCase):
    def testFixForAddLogEntry(self):
        addLogEntry(TEST_DB, TEST_USER_ID, TEST_MSG)
        objects = list(db[LOG].find())
        obj = objects[len(objects) - 1]
        self.assertEqual(type(obj[DATE]), datetime)
