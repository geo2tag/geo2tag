import requests
import json
from basic_integration_test import BasicIntegrationTest

JSON = 'json'
LAT = 'lat'
LON = 'lon'
CHANNEL_ID = 'channel_id'
ALT = 'alt'
CHANNEL_IDS_VALUE = 'channel_id_value'
TEST_URL = '/instance/service/testservice/point'
BAD_TEST_URL = '/instance/service/testservice/point'
VALID_RESPONSE_CODE = 200
GET_RESPONSE_ADRESS = '/instance/service/testservice/point/'
VALID_BC_VALUE = False
VALID_BC_VALUE1 = True


class TestBcParametrPointListPost(BasicIntegrationTest):

    def testBcPatametrPointListPost(self):
        response = requests.post(self.getUrl(TEST_URL), data=json.dumps(
            [{LAT: 1.1, LON: 1.1, ALT: 1.1, JSON: {'a': 'b'},
              CHANNEL_ID: 'channel_id_value'}]))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        responseText = response.text[2:-2]
        getResponse = requests.get(
            self.getUrl(
                GET_RESPONSE_ADRESS +
                responseText))
        self.assertEquals(getResponse.status_code, VALID_RESPONSE_CODE)
        self.assertEquals(json.loads(getResponse.text)['bc'], VALID_BC_VALUE)

        response = requests.post(self.getUrl(TEST_URL),
                                 data=json.dumps([{LAT: 1.1,
                                                   LON: 1.1,
                                                   ALT: 1.1,
                                                   JSON: {'a': 'b'},
                                                   CHANNEL_ID:
                                                       'channel_id_value',
                                                   'bc': True}]))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        responseText = response.text[2:-2]
        getResponse = requests.get(
            self.getUrl(
                GET_RESPONSE_ADRESS +
                responseText))
        self.assertEquals(getResponse.status_code, VALID_RESPONSE_CODE)
        self.assertEquals(json.loads(getResponse.text)['bc'], VALID_BC_VALUE1)
