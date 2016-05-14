from base_geo2tag_exception import BaseGeo2TagException
from werkzeug.exceptions import BadRequest


class DecodingOfTheJsonDataFailedException(BaseGeo2TagException, BadRequest):

    def getReturnObject(self):
        ERROR = 'Decoding of the JSON data failed'
        return ERROR, 400
