import requests
from flask import request
from geocoder_request_limit_exceed import GeocoderRequestLimitExceed


SEARCH_JSON = 'searchJSON?'
USERNAME = '&username='
USERNAME_VALUE = 'nikita.melnikov95@gmail.com'
Q = 'q'
STATUS_EXCEPTION = 'status'
VALUE_EXCEPTION = 'value'
ERROR_CODE_DAY_LIMIT = '18'
ERROR_CODE_HOUR_LIMIT = '19'
ERROR_CODE_WEEK_LIMIT = '20'


class GeonamesRequestSender():

    REQUEST_URL = 'http://api.geonames.org/'

    @classmethod
    def requestCoordinates(addressStringList, callback):
        callback_response = [] 
        try:
            for address in addressStringList:
                get_response = requestSingleCoordinates(address)
                callback_response.add(get_response)
        except GeocoderRequestLimitExceed:
            pass

    @classmethod
    def requestSingleCoordinates(self, address):
        response = requests.get(self.createRequestUrl(address))
        responseText = response.text
        self.checkResponseForException(responseText)

    @classmethod
    def createRequestUrl(self, address):
        url = self.REQUEST_URL + SEARCH_JSON + Q + address + USERNAME + USERNAME_VALUE
        return url

    @staticmethod
    def checkResponseForException(responseText):
        if STATUS_EXCEPTION in responseText:
            if responseText[STATUS_EXCEPTION][VALUE_EXCEPTION] == ERROR_CODE_DAY_LIMIT or responseText[STATUS_EXCEPTION][
                    VALUE_EXCEPTION] == ERROR_CODE_HOUR_LIMIT or responseText[STATUS_EXCEPTION][VALUE_EXCEPTION] == ERROR_CODE_WEEK_LIMIT:
                raise GeocoderRequestLimitExceed()
        else:
            return responseText
