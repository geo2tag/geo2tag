import requests
from basic_integration_test import BasicIntegrationTest


TEST_URL = 'instance/user/test'
VALID_RESPONSE_TEXT = 'User does not exist'


class TestGT1766FindUserInDB(BasicIntegrationTest):
    def testGT1766FindUserInDB(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
