import requests
import json
import time
from flask import request
from geocoder_request_limit_exceed import GeocoderRequestLimitExceed
from geocoder_request_other_exceed import GeocoderRequestOtherExceed
import sys
sys.path.append('../')
from config_reader import getGeonamesLogin

SEARCH_JSON = 'searchJSON?'
USERNAME = '&username='
Q = 'q='
STATUS_EXCEPTION = 'status'
VALUE_EXCEPTION = 'value'
ERROR_CODE_DAY_LIMIT = '18'
ERROR_CODE_HOUR_LIMIT = '19'
ERROR_CODE_WEEK_LIMIT = '20'
ERROR_LIST_OTHER_EXCEED = [10,11,12,13,14,15,16,17,21,22,23]

class GeonamesRequestSender():

    REQUEST_URL = 'http://api.geonames.org/'

    @classmethod
    def requestCoordinates(cls, addressStringList, geonmesLogin, callback):
        callback_response = []
        for address in addressStringList:
            try:
                get_response = cls.requestSingleCoordinates(address, geonmesLogin)
                get_response = json.loads(get_response)
                callback_response.append(get_response)
            except GeocoderRequestLimitExceed as e:
                callback(callback_response)
                callback_response = []
                time.sleep((e.lenght_to_period)*60)
        callback(callback_response)       

    @classmethod
    def requestSingleCoordinates(cls, address, geonmesLogin):
        response = requests.get(cls.createRequestUrl(address, geonmesLogin))
        responseText = response.text
        response_single = cls.checkResponseForException(responseText)
        return response_single

    @classmethod
    def createRequestUrl(cls, address, geonmesLogin):
        url = cls.REQUEST_URL + SEARCH_JSON + Q + address + USERNAME + geonmesLogin
        return url

    @classmethod
    def checkResponseForException(cls, responseText):
        if STATUS_EXCEPTION in responseText:
            responseText = json.loads(responseText)
            value_exception = responseText[STATUS_EXCEPTION][VALUE_EXCEPTION]
            if value_exception == ERROR_CODE_DAY_LIMIT:                    
                raise GeocoderRequestLimitExceed(ERROR_CODE_DAY_LIMIT, 24)
            if value_exception == ERROR_CODE_HOUR_LIMIT:                    
                raise GeocoderRequestLimitExceed(ERROR_CODE_HOUR_LIMIT, 1)
            if value_exception == ERROR_CODE_WEEK_LIMIT:                    
                raise GeocoderRequestLimitExceed(ERROR_CODE_WEEK_LIMIT, 24*7)
            if int(value_exception) in ERROR_LIST_OTHER_EXCEED:
                raise GeocoderRequestOtherExceed(value_exception)
        else:
            return responseText
