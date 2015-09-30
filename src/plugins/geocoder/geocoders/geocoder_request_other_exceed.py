import sys
sys.path.append('../')
from base_exception import BaseException


class GeocoderRequestOtherExceed(BaseException):

    def __init__(self, error_code):
        self.limit_error_code = error_code

    def getReturnObject(self):
        ERROR = "The request failed"
        return ERROR
