import requests
from basic_integration_test import BasicIntegrationTest


TEST_URL = 'instance/login'
VALID_RESPONSE_CODE = 200


class TestGT1697(BasicIntegrationTest):

    def testGT1697(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
