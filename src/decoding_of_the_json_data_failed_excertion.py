from base_geo2tag_exception import BaseGeo2TagException
from werkzeug.exceptions import BadRequest


class DecodingOfTheJsonDataFailedException(BaseGeo2TagException, BadRequest):

    def getReturnObject(self):
        ERROR = 'Decoding of the JSON data failed: JSON data request' + \
            'doesn/'t conform to the standard https://tools.ietf.org/html/rfc7159'
        return ERROR, 400
