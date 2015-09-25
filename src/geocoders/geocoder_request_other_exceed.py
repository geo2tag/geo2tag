import sys
sys.path.append('../')
from base_exception import BaseException


class GeocoderRequestOtherExceed(BaseException):

    ERROR_LIST_OTHER_EXCEED = [10,11,12,13,14,15,16,17,21,22,23]
	
    def __init__(self,error_code):
	self.limit_error_code = error_code

    def getReturnObject(self):
        ERROR = "The request failed"
        return {ERROR,self.limit_error_code}
