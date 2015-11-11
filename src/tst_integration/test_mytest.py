import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = ''
VALID_RESPONSE_CODE = 200

class TestMytest(BasicIntegrationTest):
    def testMytest(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
