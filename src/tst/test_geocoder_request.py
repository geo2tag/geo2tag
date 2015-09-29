#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest 
from geocoder_request import GeonamesRequestSender
from geocoder_request_limit_exceed import GeocoderRequestLimitExceed
from geocoder_request_other_exceed import GeocoderRequestOtherExceed
import json

TEST_SEARCH = 'asdasd'
RESPONSE_TEST_SEARCH = 'http://api.geonames.org/searchJSON?q=' + TEST_SEARCH + '&username=nikmel95@mail.ru'
TEST_ERROR_CODE = '10'
RESPONSE_SINGLE =  {"totalResultsCount":1,"geonames":[{"countryId":"2510769","adminCode1":"58","countryName":"Spain","fclName":"spot, building, farm","countryCode":"ES","lng":"-8.65049","fcodeName":"hotel","toponymName":"Asdasd","fcl":"S","name":"Asdasd","fcode":"HTL","geonameId":10172468,"lat":"42.42865","adminName1":"Galicia","population":0}]}
RESPONSE_SINGLE1 = {"totalResultsCount":1,"geonames":[{"adminCode1":"58","lng":"-8.65049","geonameId":10172468,"toponymName":"Asdasd","countryId":"2510769","fcl":"S","population":0,"countryCode":"ES","name":"Asdasd","fclName":"spot, building, farm","countryName":"Spain","fcodeName":"hotel","adminName1":"Galicia","lat":"42.42865","fcode":"HTL"}]}
COUNTRY_ID_VAL = '2510769'
GEONAMES = 'geonames'
COUNTRY_ID = 'countryId'
REQUET_ADDRESS_LIST = []
RESPONSE_FOR_LIMIT_EXCEED = {"status": {"message": "test mess","value": "19"}}
RESPONSE_FOR_OTHER_EXCEED = {"status": {"message": "test mess","value": "10"}}

def callback_test(result):
    global RESPONSE_REQUEST_COORDINATES
    RESPONSE_REQUEST_COORDINATES = result

class TestGeonamesRequestSender(unittest.TestCase):

    def test_createRequestUrl(self):
    	url = GeonamesRequestSender.createRequestUrl(TEST_SEARCH)
    	self.assertEqual(url,RESPONSE_TEST_SEARCH)

    def test_exceed_limit(self):
    	with self.assertRaises(GeocoderRequestLimitExceed) as e:
            raise GeocoderRequestLimitExceed(TEST_ERROR_CODE)

    def test_exceed_other(self):
    	with self.assertRaises(GeocoderRequestOtherExceed) as e:
            raise GeocoderRequestOtherExceed(TEST_ERROR_CODE)

    def test_requestSingleCoordinates(self):
    	response = GeonamesRequestSender.requestSingleCoordinates(TEST_SEARCH)
        response = json.loads(response)
    	self.assertEqual((response),RESPONSE_SINGLE)

    def test_requestSingleCoordinates_syntax(self):
    	response = GeonamesRequestSender.requestSingleCoordinates(TEST_SEARCH)
    	response = json.loads(response)
    	self.assertEqual(COUNTRY_ID_VAL,response[GEONAMES][0][COUNTRY_ID])

    def test_requestCoordinates(self):
    	REQUET_ADDRESS_LIST.append(TEST_SEARCH)
        REQUET_ADDRESS_LIST.append(TEST_SEARCH)
    	GeonamesRequestSender.requestCoordinates(REQUET_ADDRESS_LIST,callback_test)
        self.assertEqual(RESPONSE_REQUEST_COORDINATES[0],RESPONSE_SINGLE1)
        self.assertEqual(RESPONSE_REQUEST_COORDINATES[1],RESPONSE_SINGLE1)

    def test_exceed_limit_data(self):
        with self.assertRaises(GeocoderRequestLimitExceed) as e:
            GeonamesRequestSender.checkResponseForException(json.dumps(RESPONSE_FOR_LIMIT_EXCEED))

    def test_exceed_other_data(self):
        with self.assertRaises(GeocoderRequestOtherExceed) as e:
            GeonamesRequestSender.checkResponseForException(json.dumps(RESPONSE_FOR_OTHER_EXCEED))
