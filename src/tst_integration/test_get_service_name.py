import requests

from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/service/testservice'
TEST_NOT_VALID_URL = '/instance/service/nameservicenotvalid'

VALID_RESPONSE_CODE = 200
VALID_RESPONSE_CODE_NOT_VALID_URL = 404


class TestServiceGetRequest(BasicIntegrationTest):

    def testServiceGetRequest(self):
        response = requests.get(self.getUrl(TEST_NOT_VALID_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE_NOT_VALID_URL)
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
