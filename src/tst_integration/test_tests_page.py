import unittest
import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/tests'
VALID_RESPONSE_CODE = 200

class Test_tests_page(BasicIntegrationTest):
    def test_tests_page(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
