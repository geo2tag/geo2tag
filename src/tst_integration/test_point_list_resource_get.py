import unittest
import requests
from pymongo import MongoClient
from basic_integration_test import BasicIntegrationTest
import sys
sys.path.append('../')

import log_resource
from point_list_resource_parser import PointListResourceParser
import geo_json_type

NUMBER = 'number'
NUMBER_VALUE = 0
OFFSET = 'offset'
OFFSET_VALUE = 0
DATE_FROM = 'date_from'
DATE_FROM_VALUE = '1970-06-15T18:00:00'
DATE_TO = 'date_to'
DATE_TO_VALUE = '2015-06-15T17:00:00'
CHANNEL_IDS = 'channel_ids'
CHANNEL_IDS_VALUE = 'channel_ids_value'
GEOMETRY = 'geometry'
GEOMETRY_VALUE = '{"coordinates": [-115.8, 37.2], "type": "Point"}'
GEOMETRY_VALUE_JSON = {"coordinates": [-115.8, 37.2], "type": "Point"}

CORRECT_ARGS = NUMBER+'='+str(NUMBER_VALUE)+'&'+OFFSET+'='+str(OFFSET_VALUE)+'&'+DATE_FROM+'='+str(DATE_FROM_VALUE)+'&'+DATE_TO+'='+str(DATE_TO_VALUE)+'&'+CHANNEL_IDS+'='+CHANNEL_IDS_VALUE+'&'+GEOMETRY+'='+GEOMETRY_VALUE
TEST_URL = '/instance/service/testservice/point?' + CORRECT_ARGS
BAD_TEST_URL = '/instance/service/testservice/point'
VALID_RESPONSE_TEXT = u'{"altitude_from": null, "geometry": {"type": "Point", "coordinates": [-115.8, 37.2]}, "channel_ids": "channel_ids_value", "date_from": "\\"1970-06-15T18:00:00\\"", "offset": 0, "number": 0, "substring": null, "radius": 1000, "date_to": "\\"2015-06-15T17:00:00\\"", "altitude_to": null}'
NOT_VALID_RESPONSE_TEXT = u'{"message": "[channel_ids]: Missing required parameter in the JSON body or the post body or the query string"}'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 400
class TestPointListGetRequest(BasicIntegrationTest):
    def testPointListGetRequest(self):
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