import unittest
import requests
from pymongo import MongoClient
from basic_integration_test import BasicIntegrationTest
import sys
sys.path.append('../')

TEST_URL = '/instance/service/testservice/point'
VALID_RESPONSE_TEXT = '[]'
NOT_VALID_RESPONSE_TEXT = '[]'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 200
class TestPointListGetRequest(BasicIntegrationTest):
    def testPointListGetRequest(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)