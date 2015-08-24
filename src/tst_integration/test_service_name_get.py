import unittest
import requests
from basic_integration_test import BasicIntegrationTest
from db_model import addService, removeService
import json

TEST_SERVICE_NAME = "goodService"
TEST_SERVICE_LOG_SIZE = 10
TEST_SERVICE_OWNER_ID = "goodOwnerId"
TEST_URL = '/instance/service/' + TEST_SERVICE_NAME
VALID_RESPONSE_CODE = 200
INVALID_RESPONSE_CODE = 404


class TestServiceNameGetRequest(BasicIntegrationTest):

    def testServiceNameGetRequest(self):

        addService(
            TEST_SERVICE_NAME,
            TEST_SERVICE_LOG_SIZE,
            TEST_SERVICE_OWNER_ID)

        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseJson = json.loads(responseText)
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        self.assertEquals(responseJson['name'], TEST_SERVICE_NAME)
        self.assertEquals(
            responseJson['config']['log_size'],
            TEST_SERVICE_LOG_SIZE)
        self.assertEquals(responseJson['owner_id'], TEST_SERVICE_OWNER_ID)

        removeService(TEST_SERVICE_NAME)

        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, INVALID_RESPONSE_CODE)
