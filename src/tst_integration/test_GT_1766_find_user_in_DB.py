import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = 'instance/user/ZzKPM5GJQ1'
VALID_RESPONSE_CODE = 200
BAD_TEST_URL = 'instance/user/test'
NOT_VALID_RESPONSE_TEXT = 'User does not exist'


class TestGT1766FindUserInDB(BasicIntegrationTest):

    def testGT1766FindUserInDB(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
