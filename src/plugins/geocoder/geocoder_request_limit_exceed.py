import sys
from base_geo2tag_exception import BaseGeo2TagException


class GeocoderRequestLimitExceed(BaseGeo2TagException):

    ERROR_CODE_DAY_LIMIT = '18'
    ERROR_CODE_HOUR_LIMIT = '19'
    ERROR_CODE_WEEK_LIMIT = '20'
    limit_error_code = 0
    lenght_to_period = 0
    message_error = ''

    def __init__(self, error_code):
        self.limit_error_code = error_code
        if error_code == self.ERROR_CODE_DAY_LIMIT:
            self.lenght_to_period = 24
            self.message_error = 'Limit exceeded the number of requests per day'
        if error_code == self.ERROR_CODE_HOUR_LIMIT:
            self.lenght_to_period = 1
            self.message_error = 'Limit exceeded the number of requests per hour'
        if error_code == self.ERROR_CODE_WEEK_LIMIT:
            self.lenght_to_period = 7 * 24
            self.message_error = 'Limit exceeded the number of requests in a week'

    def getReturnObject(self):
        ERROR = 'Error code:' + self.limit_error_code + ',Status:' + self.message_error
        return ERROR
