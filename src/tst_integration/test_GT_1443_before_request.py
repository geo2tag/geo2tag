import requests
from basic_integration_test import BasicIntegrationTest
TEST_URL = '/instance/plugin/test_plugin/res1'
BAD_TEST_URL = '/instance/plugin/nonexistant_plugin/resource'
VALID_RESPONSE_TEXT = 'test_resource_1'
NOT_VALID_RESPONSE_TEXT = 'Plugin is not enabled'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 404


class Test_GT_1443_Request(BasicIntegrationTest):

    def test_GT_1443_Request(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        response = requests.get(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
