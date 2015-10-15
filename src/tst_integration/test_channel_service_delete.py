import requests
from basic_integration_test import BasicIntegrationTest

TEST_SERVICE = 'testservice'
TEST_URL = '/instance/service/testservice/channel/558807a47ec8ff5da755ee48'
BAD_TEST_URL = '/instance/service/testservice/channel/111117a47ec8115da7551111'
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = '{}'
NOT_VALID_RESPONSE_CODE = 404
NOT_VALID_RESPONSE_TEXT = "Channel does not exist"


class ChannelResourceDelete(BasicIntegrationTest):

    def testChannelResourceDelete(self):
        response = requests.delete(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.delete(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
