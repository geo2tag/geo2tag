import unittest
import requests
from pymongo import MongoClient
from basic_integration_test import BasicIntegrationTest
import sys
sys.path.append('../')
from db_model import getChannelsList
from config_reader import getHost, getPort, getDbName

TEST_SERVICE = 'testservice'
TEST_URL = '/instance/service/testservice/point/552833515c0dd1178d37f7bb'
BAD_TEST_URL = '/instance/service/testservice/point/111117a47ec8115da7551111'
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = '{}'
NOT_VALID_RESPONSE_CODE = 404
NOT_VALID_RESPONSE_TEXT = "Point does not exist"
db = MongoClient(getHost(), getPort())['testservice']

class PointResourcePut(BasicIntegrationTest):
    def testPointResourcePut(self):
        response = requests.put(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.put(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)