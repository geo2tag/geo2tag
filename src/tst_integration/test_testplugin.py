import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL1 = '/instance/plugin/test_plugin/res1'
TEST_URL2 = '/instance/plugin/test_plugin/res2'
VALID_RESPONSE_CODE = 200


class TestTestPlugin(BasicIntegrationTest):

    def testTestPlugin(self):
        response = requests.get(self.getUrl(TEST_URL1))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_URL2))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
