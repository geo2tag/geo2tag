from base_geo2tag_exception import BaseGeo2TagException


class ValueJSONException(BaseGeo2TagException, ValueError):

    def getReturnObject(self):
        return '------', 400
