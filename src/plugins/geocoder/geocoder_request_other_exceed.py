from base_geo2tag_exception import BaseGeo2TagException


class GeocoderRequestOtherExceed(BaseGeo2TagException):

    ERROR_LIST_OTHER_EXCEED = [10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23]
    other_error_code = 0
    message_error = ''

    def __init__(self, error_code):
        self.other_error_code = error_code
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[0]):
            self.message_error = 'Authorization Exception'
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[1]):
            self.message_error = 'Record does not exist'
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[2]):
            self.message_error = 'Other error'
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[3]):
            self.message_error = 'Database timeout'
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[4]):
            self.message_error = 'Invalid parameter'
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[5]):
            self.message_error = 'No result found'
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[6]):
            self.message_error = 'Duplicate exception'
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[7]):
            self.message_error = 'Postal code not found'
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[8]):
            self.message_error = 'Invalid input'
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[8]):
            self.message_error = 'Server overloaded exception'
        if error_code == str(self.ERROR_LIST_OTHER_EXCEED[10]):
            self.message_error = 'Service not implemented'

    def getReturnObject(self):
        ERROR = 'Error code:' + self.other_error_code + ',Status:' + self.message_error
        return ERROR
