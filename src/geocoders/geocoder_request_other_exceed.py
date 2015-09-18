import sys
sys.path.append('../')
from base_exception import BaseException


class GeocoderRequestOtherExceed(BaseException):

    def getReturnObject(self):
        ERROR = "The request failed"
        return ERROR
