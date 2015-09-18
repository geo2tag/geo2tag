import requests
import json
from flask import request
from geocoder_request_limit_exceed import GeocoderRequestLimitExceed
from geocoder_request_other_exceed import GeocoderRequestOtherExceed

SEARCH_JSON = 'searchJSON?'
USERNAME = '&username='
USERNAME_VALUE = 'nikmel95@mail.ru'
Q = 'q='
STATUS_EXCEPTION = 'status'
VALUE_EXCEPTION = 'value'
ERROR_CODE_DAY_LIMIT = '18'
ERROR_CODE_HOUR_LIMIT = '19'
ERROR_CODE_WEEK_LIMIT = '20'


class GeonamesRequestSender():

    REQUEST_URL = 'http://api.geonames.org/'

    @classmethod
    def requestCoordinates(cls, addressStringList, callback):
        callback_response = [] 
        try:
            for address in addressStringList:
                get_response = cls.requestSingleCoordinates(address)
                callback_response.append(get_response)
            callback(callback_response)
        except GeocoderRequestLimitExceed:
            callback(callback_response)

    @classmethod
    def requestSingleCoordinates(cls, address):
        response = requests.get(cls.createRequestUrl(address))
        responseText = response.text
        response_single = cls.checkResponseForException(responseText)
        return response_single

    @classmethod
    def createRequestUrl(cls, address):
        url = cls.REQUEST_URL + SEARCH_JSON + Q + address + USERNAME + USERNAME_VALUE
        return url

    @staticmethod
    def checkResponseForException(responseText):
        if STATUS_EXCEPTION in responseText:
            responseText = json.loads(responseText)
            value_exception = responseText[STATUS_EXCEPTION][VALUE_EXCEPTION]
            if value_exception == ERROR_CODE_DAY_LIMIT:                    
                raise GeocoderRequestLimitExceed(ERROR_CODE_DAY_LIMIT)
            if value_exception == ERROR_CODE_HOUR_LIMIT:                    
                raise GeocoderRequestLimitExceed(ERROR_CODE_HOUR_LIMIT)
            if value_exception == ERROR_CODE_WEEK_LIMIT:                    
                raise GeocoderRequestLimitExceed(ERROR_CODE_WEEK_LIMIT)
            if int(value_exception) in range(10,17) and int(value_exception) in range(21,23):
                raise GeocoderRequestOtherExceed(value_exception)
        else:
            return responseText
