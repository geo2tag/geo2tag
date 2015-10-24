from db_model import addLogEntry, getDbObject, getClientObject
from config_reader import getDbName
from log import writeInstanceLog
from log import writeServiceLog
from log import LOG_LVL_INFO
from log import LOG_LVL_WARNING
from log import LOG_LVL_ERROR
from log import LOG_LVL_CRITICAL
import unittest
from pymongo import DESCENDING

# VALUES
TEST_USER_ID = 'test_user_id'
TEST_MSG = 'test_msg'
TEST_SERVICE = 'service'

# FIELDS
TEST_USER_ID_FIELD = 'user_id'
TEST_MSG_FIELD = 'message'
TEST_SERVICE_FIELD = 'service'
TEST_LEVEL_FIELD = 'level'
TEST_SERVICE = 'testservice'

# COLLECTIONS
LOG = 'log'

glog = getDbObject()[LOG]
tslog = getDbObject('testservice')[LOG]


class TestLogLvl(unittest.TestCase):

    def testLogLvlIstanceLog(self):
        writeInstanceLog(TEST_USER_ID, TEST_MSG, LOG_LVL_INFO)
        obj = list(glog.find().sort('_id', DESCENDING).limit(1))[0]
        self.assertEqual(obj[TEST_LEVEL_FIELD], LOG_LVL_INFO)
        writeInstanceLog(TEST_USER_ID, TEST_MSG, LOG_LVL_WARNING)
        obj = list(glog.find().sort('_id', DESCENDING).limit(1))[0]
        self.assertEqual(obj[TEST_LEVEL_FIELD], LOG_LVL_WARNING)
        writeInstanceLog(TEST_USER_ID, TEST_MSG, LOG_LVL_ERROR)
        obj = list(glog.find().sort('_id', DESCENDING).limit(1))[0]
        self.assertEqual(obj[TEST_LEVEL_FIELD], LOG_LVL_ERROR)
        writeInstanceLog(TEST_USER_ID, TEST_MSG, LOG_LVL_CRITICAL)
        obj = list(glog.find().sort('_id', DESCENDING).limit(1))[0]
        self.assertEqual(obj[TEST_LEVEL_FIELD], LOG_LVL_CRITICAL)

    def testLogLvlServiceLog(self):
        writeServiceLog(TEST_SERVICE, TEST_USER_ID, TEST_MSG, LOG_LVL_INFO)
        obj = list(tslog.find().sort('_id', DESCENDING).limit(1))[0]
        self.assertEqual(obj[TEST_LEVEL_FIELD], LOG_LVL_INFO)
        writeServiceLog(TEST_SERVICE, TEST_USER_ID, TEST_MSG, LOG_LVL_WARNING)
        obj = list(tslog.find().sort('_id', DESCENDING).limit(1))[0]
        self.assertEqual(obj[TEST_LEVEL_FIELD], LOG_LVL_WARNING)
        writeServiceLog(TEST_SERVICE, TEST_USER_ID, TEST_MSG, LOG_LVL_ERROR)
        obj = list(tslog.find().sort('_id', DESCENDING).limit(1))[0]
        self.assertEqual(obj[TEST_LEVEL_FIELD], LOG_LVL_ERROR)
        writeServiceLog(TEST_SERVICE, TEST_USER_ID, TEST_MSG, 
            LOG_LVL_CRITICAL)
        obj = list(tslog.find().sort('_id', DESCENDING).limit(1))[0]
        self.assertEqual(obj[TEST_LEVEL_FIELD], LOG_LVL_CRITICAL)
