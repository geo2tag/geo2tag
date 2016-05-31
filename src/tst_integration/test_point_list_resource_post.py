import requests
import unittest
import sys
from basic_integration_test import BasicIntegrationTest
from json import loads, dumps

DB = "testservice"
COLLECTION = 'points'
JSON = 'json'
LAT = 'lat'
LON = 'lon'
CHANNEL_ID = 'channel_id'
ALT = 'alt'
CHANNEL_IDS_VALUE = '55671ae113293c504d514a53'
TEST_URL = '/instance/service/testservice/point'
BAD_TEST_URL = '/instance/service/testservice/point'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 400
RESPONSE_TEXT_INVALID = u'"\'lat\' - Incorrect type"'


class TestPointListPostRequest(BasicIntegrationTest):

    def testPointListPostRequestValid(self):
        pointAddResponse = requests.post(self.getUrl(TEST_URL), data=dumps(
            [{
                LAT: 1.1,
                LON: 1.1,
                ALT: 1.1,
                JSON: {'a': 'b'},
                CHANNEL_ID: '55671ae113293c504d514a53'
            }]))
        responseCode = pointAddResponse.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        responseText = pointAddResponse.text
        print responseText
        validId = loads(responseText)[0]
        # Check if added points are available at REST interfaces
        singlePointResponse = requests.get(
            self.getUrl(TEST_URL + '/' + validId))
        recievedPointCode = singlePointResponse.status_code
        self.assertEquals(recievedPointCode, VALID_RESPONSE_CODE)

    def testPointListPostRequestInvalid(self):
        response = requests.post(self.getUrl(TEST_URL), data=dumps(
            [{LAT: '1.1', LON: 1.1, ALT: 1.1, JSON: [], CHANNEL_ID:''}]))
        responseCode = response.status_code
        responseText = response.text
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
        self.assertEquals(responseText, RESPONSE_TEXT_INVALID)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(
        BasicIntegrationTest.parametrize(
            TestPointListPostRequest, param='http://geomongo/'))
    returnCode = not unittest.TextTestRunner(
        verbosity=2).run(suite).wasSuccessful()

    sys.exit(returnCode)
