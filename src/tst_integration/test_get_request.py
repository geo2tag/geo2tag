import sys
import unittest
import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/service/'
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = '[]'

class TestServiceListRequest(BasicIntegrationTest):
    def testServiceListRequest(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        