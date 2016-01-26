import unittest
from db_model import getPluginInfo, getDbObject, ENABLED, CONFIGURABLE


TEST_PLUGIN_NAME = 'test_plugin_name_gt_1793'
TEST_VALID_RESULT_FALSE = {ENABLED: False, CONFIGURABLE: True} 
TEST_PLUGINS_COLLECTION = 'plugins'
TEST_VALUE = True
db = getDbObject()
NAME = 'name'
TEST_VALID_RESULT = {ENABLED: TEST_VALUE, CONFIGURABLE: TEST_VALUE}


class TestGetPluginInfoFromDBModel(unittest.TestCase):

    def testGetPluginInfoFromDBModel(self):
        result = getPluginInfo(TEST_PLUGIN_NAME)
        self.assertEquals(result, TEST_VALID_RESULT_FALSE)
        db[TEST_PLUGINS_COLLECTION].insert(
            {NAME: TEST_PLUGIN_NAME, ENABLED: TEST_VALUE,
                CONFIGURABLE: TEST_VALUE})
        db[TEST_PLUGINS_COLLECTION].find({NAME: TEST_PLUGIN_NAME})
        result = getPluginInfo(TEST_PLUGIN_NAME)
        self.assertEquals(result, TEST_VALID_RESULT)
        db[TEST_PLUGINS_COLLECTION].remove({NAME: TEST_PLUGIN_NAME})
