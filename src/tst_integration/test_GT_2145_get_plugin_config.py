import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/admin/plugin/config/test_plugin'
TEST_NOT_VALID_URL = '/instance/admin/plugin/config'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 400


class TestUserListResource(BasicIntegrationTest):

    def testUserListResource(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_NOT_VALID_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
