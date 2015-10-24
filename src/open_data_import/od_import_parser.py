import os
from flask_restful import request
from json import loads
from werkzeug.exceptions import BadRequest
CHANNEL_NAME = 'channelName'
OPEN_DATA_URL = 'openDataUrl'


class OdImportParser():

    mandatoryFields = [CHANNEL_NAME, OPEN_DATA_URL]

    @classmethod
    def parsePostParameters(cls):
        print "-----parsePostParameters"
        print os.getcwd()
        args = loads(request.get_data())
        for key in cls.mandatoryFields:
            if key not in args:
                raise BadRequest('{0} parameter is missing'.format(key))
            elif not isinstance(args[key], unicode):
                raise BadRequest('{0} value is not unicode'.format(key))

        return args
