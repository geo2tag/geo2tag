import requests
from flask import request
from geocoder_request_limit_exceed import GeocoderRequestLimitExceed

REQUST_URL = 'http://api.geonames.org/searchJSON?'
USERNAME = '&username='
USERNAME_VALUE = 'nikita.melnikov95@gmail.com'
Q = 'q'
STATUS_EXCEPTION = 'status'
VALUE_EXCEPTION = 'value'
ERROR_CODE_DAY_LIMIT = '18'
ERROR_CODE_HOUR_LIMIT = '19'
ERROR_CODE_WEEK_LIMIT = '20'


class GeonamesRequestSender():

    @staticmethod
    def requestSingleCoordinates(adress):
        response = requests.get(REQUST_URL + Q + '=' +
                                adress + USERNAME + USERNAME_VALUE)
        responseText = response.text
        if STATUS_EXCEPTION in responseText:
            if responseText[STATUS_EXCEPTION][VALUE_EXCEPTION] == ERROR_CODE_DAY_LIMIT or responseText[STATUS_EXCEPTION][
                    VALUE_EXCEPTION] == ERROR_CODE_HOUR_LIMIT or responseText[STATUS_EXCEPTION][VALUE_EXCEPTION] == ERROR_CODE_WEEK_LIMIT:
                raise GeocoderRequestLimitExceed()
        else:
            return responseText
