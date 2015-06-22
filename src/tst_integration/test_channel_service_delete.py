import unittest
import requests
from basic_integration_test import BasicIntegrationTest
import sys
sys.path.append('../')
from db_model import getChannelsList

TEST_SERVICE = 'testservice'
TEST_URL = '/instance/service/testservice/channel/'
BAD_TEST_URL = '/instance/service/testservice/channel/test_channel_id'
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = '{}'
NOT_VALID_RESPONSE_CODE = 404
NOT_VALID_RESPONSE_TEXT = "Channel does not exist"

class ChannelResourceDelete(BasicIntegrationTest):
    def testChannelResourceDelete(self):
    	result = list(getChannelsList(TEST_SERVICE, 'test_channel_1', None, None))
    	TEST_URL2 = TEST_URL + str(result[0].get('_id')) + '/'
        response = requests.delete(self.getUrl(TEST_URL2))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.delete(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        print responseText, responseCode
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)