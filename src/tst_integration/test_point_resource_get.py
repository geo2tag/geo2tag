import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/service/testservice/point/552833515c0dd1178d37f7aa'
BAD_TEST_URL = '/instance/service/testservice/point/112833515c0dd11711111111'
VALID_RESPONSE_TEXT = \
    '{"date": {"$date": 1428708737813}, ' \
    '"_id": {"$oid": "552833515c0dd1178d37f7aa"}, ' \
    '"location": {"type": "Point", ' \
    '"coordinates": [22, 2.4]}, "bc": false, "name": ""}'
NOT_VALID_RESPONSE_TEXT = 'Point does not exist'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 404


class TestPointGetRequest(BasicIntegrationTest):

    def testPointGetRequest(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
