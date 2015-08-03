import unittest
import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/service/testservice/point'

VALID_PARAMS = '?number=100&channel_ids=556721a52a2e7febd2744202&channel_ids=556721a52a2e7febd2744201&date_from=2015-09-10T23:32:17&date_to=2015-09-11T23:32:17'
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = '[]'
VALID_RESPONSE_TEXT_LEN = 3
PARSE_LIST_PARAM = '"}}, {"'

INVALID_PARAMS = '?number=100'
INVALID_RESPONSE_CODE = 400 
INVALID_RESPONSE_TEXT = '{"message": "[channel_ids]: Missing required parameter in the JSON body or the post body or the query string"}'


class TestPointListGet_ResponseText(BasicIntegrationTest):
    def testValid(self):
        response = requests.get(self.getUrl(TEST_URL + VALID_PARAMS))
        responseText = response.text
        responseCode = response.status_code
        len_l =  len(list(responseText.split(PARSE_LIST_PARAM)))
        self.assertEquals(VALID_RESPONSE_TEXT_LEN, len_l)
        self.assertEquals(VALID_RESPONSE_CODE, responseCode)

    def testInvalid(self):
        response = requests.get(self.getUrl(TEST_URL + INVALID_PARAMS))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(INVALID_RESPONSE_CODE, responseCode)
        self.assertEquals(responseText, INVALID_RESPONSE_TEXT)