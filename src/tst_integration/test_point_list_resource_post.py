import unittest
import requests, json
from pymongo import MongoClient
from flask import Flask, request
from basic_integration_test import BasicIntegrationTest
import sys
sys.path.append('../')
from point_parsers import PointParser

app = Flask(__name__)

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
TEST_URL = '/instance/service/testservice/point/'
BAD_TEST_URL = '/instance/service/testservice/point/?'
VALID_RESPONSE_TEXT = '[{lat:1.1, lon:1.1, alt:1.1,json:{}, channel_id:  }]'
NOT_VALID_RESPONSE_TEXT = ''
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 400
class TestPointListPostRequest(BasicIntegrationTest):
    def testPointListPostRequest(self):
        with app.test_request_context(TEST_URL, data =  '[{lat:1.1, lon:1.1, alt:1.1,json:{}, channel_id:''  }]', method='POST'):
            responseText = request.data
            self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        with app.test_request_context(TEST_URL, data =  '', method='POST'):
            d = request.get_json()
            responseText = request.data
            self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)