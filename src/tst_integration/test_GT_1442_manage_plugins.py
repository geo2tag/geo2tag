import sys
import unittest
import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/manage_plugins?test_plugin=True&testPlugin1=False'
TEST_URL2 = '/instance/manage_plugins?test_plugin=True&testPlugin=False'
VALID_TEXT = 'null'
EXIST_NAME = 'testservice'
DATA = {'name': VALID_TEXT}
DATA2 = {'name': EXIST_NAME}
VALID_RESPONSE_TEXT = u'[{"json": {}, "_id": {"$oid": "556721a52a2e7febd2744204"}, "name": "test_channel_4", "owner_id": "STUB"}, {"json": {}, "_id": {"$oid": "556721a52a2e7febd2744203"}, "name": "test_channel_5", "owner_id": "STUB"}]'
NOT_VALID_RESPONSE_TEXT = u'{"message": "[offset]: invalid literal for int() with base 10: \'str\'"}'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 400
class Test_GT_1442_managePlugins(BasicIntegrationTest):
    def test_GT_1442_managePlugins(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(VALID_TEXT, responseText)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_URL2))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(VALID_TEXT, responseText)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)