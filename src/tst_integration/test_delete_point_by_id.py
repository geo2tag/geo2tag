import requests
from basic_integration_test import BasicIntegrationTest
import json

TEST_SERVICE = 'testservice'
COLLECTION = 'points'
NAME = 'name'
NAME_TEST_OBJECT = 'test_GT_1307'
TEST_URL = '/instance/service/testservice/point'
BAD_TEST_URL = '/instance/service/testservice/point/111117a47ec8115da7551111'
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = '{}'
NOT_VALID_RESPONSE_CODE = 404
NOT_VALID_RESPONSE_TEXT = "Point does not exist"
LAT = 'lat'
LON = 'lon'
ALT = 'alt'
JSON = 'json'
CHANNEL_ID = 'channel_id'
TEST_URL_DEL = '/instance/service/testservice/point/'


def getObjectIdFromResponse(response):
    return response._content[2:26]


class TestPointResourceDelete(BasicIntegrationTest):

    def testPointResourceDelete(self):
        response = requests.post(self.getUrl(TEST_URL), data=json.dumps(
            [{
                LAT: 1.1,
                LON: 1.1,
                ALT: 1.1,
                JSON: {'ac': 'dc'},
                CHANNEL_ID: '55671ae113293c504d515a53'
            }]))
        obj_id = getObjectIdFromResponse(response)
        response = requests.delete(self.getUrl(TEST_URL_DEL + unicode(obj_id)))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.delete(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
