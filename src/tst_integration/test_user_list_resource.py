import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/user'
VALID_RESPONSE_CODE = 200


class TestUserListResource(BasicIntegrationTest):

    def testUserListResource(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
