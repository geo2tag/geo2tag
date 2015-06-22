import unittest
import requests
from pymongo import MongoClient
from basic_integration_test import BasicIntegrationTest
import sys
sys.path.append('../')
from db_model import getChannelsList
from config_reader import getHost, getPort, getDbName

TEST_SERVICE = 'testservice'
TEST_URL = '/instance/service/testservice/channel/'
BAD_TEST_URL = '/instance/service/testservice/channel/test_channel_id'
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = '{}'
NOT_VALID_RESPONSE_CODE = 404
NOT_VALID_RESPONSE_TEXT = "Channel does not exist"
db = MongoClient(getHost(), getPort())['testservice']

class ChannelResourceDelete(BasicIntegrationTest):
    def testChannelResourceDelete(self):
        #db['channels'].insert({"name" : "test_channel_GT-1290", "json" : {  }, "owner_id" : "STUB"})
    	result = list(db['channels'].find({'name': 'test_channel_GT-1290'}))
        print result
    	TEST_URL2 = TEST_URL + str(result[0].get('_id')) + '/'
        print TEST_URL2
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