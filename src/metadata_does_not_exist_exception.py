from base_geo2tag_exception import BaseGeo2TagException


class MetadataDoesNotExistException(BaseGeo2TagException):

    def getReturnObject(self):
        ERROR = 'Metadata Does Not Exist'
        return ERROR, 404
