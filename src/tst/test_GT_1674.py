#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest 
import sys
sys.path.append('../geocoders/')
from geocoder_request import GeonamesRequestSender
from geocoder_request_limit_exceed import GeocoderRequestLimitExceed
from geocoder_request_other_exceed import GeocoderRequestOtherExceed
import json

RESPONSE_FOR_LIMIT_EXCEED_DAY = {"status": {"message": "test mess","value": "18"}}
RESPONSE_FOR_LIMIT_EXCEED_HOUR = {"status": {"message": "test mess","value": "19"}}
RESPONSE_FOR_LIMIT_EXCEED_WEEK = {"status": {"message": "test mess","value": "20"}}
HOUR_PERIOD = 1
DAY_PERIOD = 24
WEEK_PERIOD = 7*24
DAY_ERROR_MESSAGE = ['18', 'Limit exceeded the number of requests per day']
HOUR_ERROR_MESSAGE = ['19', 'Limit exceeded the number of requests per hour']
WEEK_ERROR_MESSAGE = ['20', 'Limit exceeded the number of requests in a week']


class TestGeonamesRequestSender_LimitExcept(unittest.TestCase):

    def test_exceed_limit_hour_period(self):
        try:
            GeonamesRequestSender.checkResponseForException(json.dumps(RESPONSE_FOR_LIMIT_EXCEED_HOUR))
        except GeocoderRequestLimitExceed as e:	
	    self.assertEqual(HOUR_PERIOD,e.lenght_to_period)
	    self.assertEqual(list(e.getReturnObject()),HOUR_ERROR_MESSAGE)

    def test_exceed_limit_day_period(self):
        try:
            GeonamesRequestSender.checkResponseForException(json.dumps(RESPONSE_FOR_LIMIT_EXCEED_DAY))
        except GeocoderRequestLimitExceed as e:	
	    self.assertEqual(DAY_PERIOD,e.lenght_to_period)
	    self.assertEqual(list(e.getReturnObject()),DAY_ERROR_MESSAGE)
	    	
    def test_exceed_limit_week_period(self):
        try:
            GeonamesRequestSender.checkResponseForException(json.dumps(RESPONSE_FOR_LIMIT_EXCEED_WEEK))
        except GeocoderRequestLimitExceed as e:	
	    self.assertEqual(WEEK_PERIOD,e.lenght_to_period)
	    self.assertEqual(list(e.getReturnObject()),WEEK_ERROR_MESSAGE)
