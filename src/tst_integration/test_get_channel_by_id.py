import unittest
import requests
from basic_integration_test import BasicIntegrationTest
from config_reader import getHost, getPort, getDbName
from db_model import getDbObject

TEST_SERVICE = 'testservice'
TEST_URL = '/instance/service/testservice/channel'
BAD_TEST_URL = '/instance/service/testservice/channel/111117a47ec8115da7551111'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 404
NOT_VALID_RESPONSE_TEXT = "Channel does not exist"
CHANNELS_COLLECTION = 'channels'


class TestChannelGetRequest(BasicIntegrationTest):

    def testChannelGetRequest(self):
        db = getDbObject(TEST_SERVICE)
        obj_id = db[CHANNELS_COLLECTION].save(
            {'name': 'test_get_channel_by_id'})
        response = requests.get(self.getUrl(TEST_URL + '/' + str(obj_id)))
        VALID_RESPONSE_TEXT = '{"_id": {"$oid": "' + \
            str(obj_id) + '"}, "name": "test_get_channel_by_id"}'
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
