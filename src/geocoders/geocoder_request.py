import requests
import json
import time
from flask import request
from geocoder_request_limit_exceed import GeocoderRequestLimitExceed
from geocoder_request_other_exceed import GeocoderRequestOtherExceed

SEARCH_JSON = 'searchJSON?'
USERNAME = '&username='
Q = 'q='
STATUS_EXCEPTION = 'status'
VALUE_EXCEPTION = 'value'
DAY_ERROR_CODE = GeocoderRequestLimitExceed.ERROR_CODE_DAY_LIMIT
HOUR_ERROR_CODE = GeocoderRequestLimitExceed.ERROR_CODE_HOUR_LIMIT
WEEK_ERROR_CODE = GeocoderRequestLimitExceed.ERROR_CODE_WEEK_LIMIT
OTHER_ERROR_CODE_LIST = GeocoderRequestOtherExceed.ERROR_LIST_OTHER_EXCEED

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
            if value_exception == DAY_ERROR_CODE:                    
                raise GeocoderRequestLimitExceed(DAY_ERROR_CODE)
            if value_exception == HOUR_ERROR_CODE:                    
                raise GeocoderRequestLimitExceed(HOUR_ERROR_CODE)
            if value_exception == WEEK_ERROR_CODE:                    
                raise GeocoderRequestLimitExceed(WEEK_ERROR_CODE)
            if int(value_exception) in OTHER_ERROR_CODE_LIST:
                raise GeocoderRequestOtherExceed(OTHER_ERROR_CODE_LIST)
        else:
            return responseText
