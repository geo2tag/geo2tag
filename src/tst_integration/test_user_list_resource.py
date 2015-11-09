import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/user?number=1&offset=0&login=test_login'
TEST_NOT_VALID_URL = '/instance/user?number=1&offset=0'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 404

class TestUserListResource(BasicIntegrationTest):

    def testUserListResource(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_NOT_VALID_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
