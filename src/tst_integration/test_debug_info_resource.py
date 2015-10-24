import requests
import string

from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/debug_info'

VALID_RESPONSE_CODE = 200


class TestDebugInfoResource(BasicIntegrationTest):

    def testDebugInfoResource(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        responseText = response.text
        index = string.find(responseText, "branch")
        self.assertGreater(index, 0)
