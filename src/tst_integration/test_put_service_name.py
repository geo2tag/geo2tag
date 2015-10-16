import unittest
import requests
from basic_integration_test import BasicIntegrationTest
from db_model import removeService

TEST_URL = '/instance/service/testservice'
DATA = {'logSize': 10}
DATA2 = {'logSize': 'string'}
VALID_RESPONSE_TEXT = '{"testservice": "Service updated"}'
EXIST_RESPONSE_TEXT = '{"message": "[logSize]: invalid literal ' \
                      'for int() with base 10: \'string\'"}'
VALID_RESPONSE_CODE = 200
EXIST_RESPONSE_CODE = 400


class TestServicePutRequest(BasicIntegrationTest):

    def testServicePutRequest(self):
        response = requests.put(self.getUrl(TEST_URL), data=DATA)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.put(self.getUrl(TEST_URL), data=DATA2)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, EXIST_RESPONSE_TEXT)
        self.assertEquals(responseCode, EXIST_RESPONSE_CODE)
