from base_geo2tag_exception import BaseGeo2TagException


class ValueJSONException(BaseGeo2TagException):

    def getReturnObject(self):
        return unicode(self), 400
