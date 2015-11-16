import requests
from basic_integration_test import BasicIntegrationTest
import json

SUBSTRING = "substring"
TEST_SERVICE_NAME = "testservice"
TEST_URL = '/instance/service?' + SUBSTRING + "=" + TEST_SERVICE_NAME
VALID_RESPONSE_CODE = 200
INVALID_RESPONSE_CODE = 404


class TestServiceSearchBySubstr(BasicIntegrationTest):

    def testServiceSearchBySubstr(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseJson = json.loads(responseText)
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        self.assertEquals(responseJson[0]['name'], TEST_SERVICE_NAME)
        self.assertEquals(len(responseJson), 1)
