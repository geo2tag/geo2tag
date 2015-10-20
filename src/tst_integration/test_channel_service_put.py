import requests
from basic_integration_test import BasicIntegrationTest

TEST_SERVICE = 'testservice'
TEST_URL = '/instance/service/testservice/channel/558807a47ec8ff5da755ee47'
BAD_TEST_URL = '/instance/service/testservice/channel/111117a47ec8115da7551111'
LIST_ARGS = {'name': 'test_channel_GT-1290_put'}
BAD_LIST_ARGS = {'name': 'test_channel_GT-1290_2'}
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = '{}'
NOT_VALID_RESPONSE_CODE = 404
NOT_VALID_RESPONSE_TEXT = "Channel does not exist"


class ChannelResourcePut(BasicIntegrationTest):

    def testChannelResourcePut(self):
        response = requests.put(self.getUrl(TEST_URL), data=LIST_ARGS)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.put(self.getUrl(BAD_TEST_URL), data=BAD_LIST_ARGS)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
