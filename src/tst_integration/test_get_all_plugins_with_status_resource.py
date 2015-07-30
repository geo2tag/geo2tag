import unittest
import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/get_all_plugins_with_status_resource'
VALID_RESPONSE_CODE = 200

class TestGetAllPluginsWithStatusResource(BasicIntegrationTest):
    def testGetAllPluginsWithStatusResource(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
