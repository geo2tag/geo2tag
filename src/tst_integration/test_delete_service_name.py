import unittest
import requests
import sys
sys.path.append('../')
from db_model import addService
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/service/testservice_1'
TEST_NOT_VALID_URL = '/instance/service/nameservicenotvalid'

VALID_RESPONSE_CODE = 200
VALID_RESPONSE_CODE_NOT_VALID_URL = 404


class TestServiceDeleteRequest(BasicIntegrationTest):

    def testServiceDeleteRequest(self):
        response = requests.delete(self.getUrl(TEST_NOT_VALID_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE_NOT_VALID_URL)
        addService('testservice_1', 1, 1)
        response = requests.delete(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_URL))
