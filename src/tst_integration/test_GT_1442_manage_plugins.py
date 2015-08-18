import sys
import unittest
import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/manage_plugins?test_plugin=False&testPlugin1=True'
TEST_URL2 = '/instance/manage_plugins?test_plugin_not_valid_name=True'
VALID_TEXT = 'null'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 500


class Test_GT_1442_managePlugins(BasicIntegrationTest):

    def test_GT_1442_managePlugins(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(VALID_TEXT, responseText)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
# https://geo2tag.atlassian.net/browse/GT-1489
#        response = requests.get(self.getUrl(TEST_URL2))
#        responseCode = response.status_code
#        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
