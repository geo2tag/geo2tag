import requests
from basic_integration_test import BasicIntegrationTest

INVALID_RESPONSE_CODE = 400
VALID_RESPONSE_CODE = 200
TEST_URL = '/instance/plugin/smartm3/service/testservice/point'
VALID_PARAMS = '?number=100' \
               '&channel_ids=556721a52a2e7febd2744202' \
               '&channel_ids=556721a52a2e7febd2744201' \
               '&altitude_from=1.1'
INVALID_PARAMS = '?number=100'


class TestSmartM3Plugin(BasicIntegrationTest):

    def testValid(self):
        response = requests.get(self.getUrl(TEST_URL + VALID_PARAMS))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)

    def testInvalid(self):
        response = requests.get(self.getUrl(TEST_URL + INVALID_PARAMS))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, INVALID_RESPONSE_CODE)
