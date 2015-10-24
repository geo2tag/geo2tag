import unittest
import requests
from basic_integration_test import BasicIntegrationTest

TEST_URL = '/instance/service/testservice/point'

VALID_PARAMS = '?number=100' \
               '&channel_ids=556721a52a2e7febd2744202' \
               '&channel_ids=556721a52a2e7febd2744201' \
               '&altitude_from=1.1'
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = \
    '[{"bc": false, ' \
    '"channel_id": {"$oid": "556721a52a2e7febd2744201"},' \
    ' "json": {"image_url": "https://www.drupal.org/' \
    'files/hr10_sample_image_02_original.jpg",' \
    ' "description": "testGT-1332"}, ' \
    '"location": {"type": "Point", ' \
    '"coordinates": [1, 1]}, ' \
    '"date": {"$date": 1441927937814},' \
    ' "alt": 2, "_id": {"$oid": "55a624c69bf770b58a355f08"}}, ' \
    '{"bc": false, "channel_id": {"$oid": "556721a52a2e7febd2744202"}, ' \
    '"json": {"image_url": "http://www.dunbartutoring.com/wp-content/' \
    'themes/thesis/rotator/sample-1.jpg", "description": "testGT-1332"}, ' \
    '"location": {"type": "Point", "coordinates": [1.3, 1]},' \
    ' "date": {"$date": 1441927937814}, "alt": 2,' \
    ' "_id": {"$oid": "55a624ce9bf770b58a355f0a"}}]'

INVALID_PARAMS = '?number=100'
INVALID_RESPONSE_CODE = 400
INVALID_RESPONSE_TEXT =\
    '{"message": "[channel_ids]: Missing required parameter in the JSON' \
    ' body or the post body or the query string"}'


class TestPointListGet(BasicIntegrationTest):

    def testValid(self):
        response = requests.get(self.getUrl(TEST_URL + VALID_PARAMS))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)

    def testInvalid(self):
        response = requests.get(self.getUrl(TEST_URL + INVALID_PARAMS))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, INVALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, INVALID_RESPONSE_CODE)
