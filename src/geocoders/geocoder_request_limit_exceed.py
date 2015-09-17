import sys
sys.path.append('../')
from base_exception import BaseException


class GeocoderRequestLimitExceed(BaseException):

    def getReturnObject(self):
        ERROR = "Limit exceeded request"
        return ERROR
