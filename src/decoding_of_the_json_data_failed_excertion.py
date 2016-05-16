from base_geo2tag_exception import BaseGeo2TagException
from werkzeug.exceptions import BadRequest

URL = "https://tools.ietf.org/html/rfc7159"


class DecodingOfTheJsonDataFailedException(BaseGeo2TagException, BadRequest):

    def getReturnObject(self):
        ERROR = "Decoding of the JSON data failed: JSON data request" + \
            "doesn't conform to the standard " + URL
        return ERROR, 400
