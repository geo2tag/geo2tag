import sys
sys.path.append('../')
from base_exception import BaseException


class GeocoderRequestLimitExceed(BaseException):

    limit_error_code = 0
    lenght_to_period = 0
    def __init__(self,error_code, lenght_to_period):
	self.limit_error_code = error_code
	self.lenght_to_period = lenght_to_period

    def getReturnObject(self):
        ERROR = "Limit exceeded request"
        return ERROR
