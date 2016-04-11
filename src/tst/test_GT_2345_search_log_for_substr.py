import unittest
from db_model import getLog, addLogEntry
from log import LOG_LVL_INFO

# FIELDS
TEST_USER_ID_FIELD = 'user_id'
TEST_MSG_FIELD = u'message'
TEST_SERVICE_FIELD = 'service'
TEST_LEVEL_FIELD = 'level'

# VALUES
TEST_USER_ID = 'test_user_id'
TEST_MSG = 'test_msg_GT_2345'
TEST_SERVICE = 'service'
TEST_LOG_LEVEL_INFO = LOG_LVL_INFO
SUBSTRING = 'GT_2345'

# DB
TEST_DB = 'testservice'


class TestSearchLogForSubstr(unittest.TestCase):

    def testSearchLogForSubstr(self):
        addLogEntry(TEST_DB, TEST_USER_ID, TEST_MSG, LOG_LVL_INFO)
        result = list(getLog(TEST_DB, 1, 0, None, None, SUBSTRING))[0]
        self.assertEqual(result[TEST_MSG_FIELD], TEST_MSG)
