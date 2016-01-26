import requests
from basic_integration_test import BasicIntegrationTest
import json

TEST_SERVICE = 'testservice'
TEST_URL = '/instance/service/testservice/channel'
BAD_TEST_URL = '/instance/service/testservice/channel/111117a47ec8115da7551111'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 404
NOT_VALID_RESPONSE_TEXT = "Channel does not exist"
CHANNELS_COLLECTION = 'channels'
NAME = "test_get_channel_by_id"
JSON = "{'a':'aa'}"
DATA = {'name': NAME, 'json': JSON, 'acl': 777}
ID_KEY = u'$oid'


class TestChannelGetRequest(BasicIntegrationTest):

    def testChannelGetRequest(self):
        response = requests.post(self.getUrl(TEST_URL), data=DATA)
        responseText = response.text
        ID = json.loads(responseText)[ID_KEY]
        response = requests.get(self.getUrl(TEST_URL + '/' + unicode(ID)))
        responseText = json.loads(response.text)
        responseCode = response.status_code
        self.assertEquals(responseText['name'], NAME)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
