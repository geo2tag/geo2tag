from flask_restful import request
from json import loads

CHANNEL_NAME = 'channelName'
OPEN_DATA_URL = 'openDataUrl'
SHOW_OBJECT_URL = 'showObjectUrl'
SHOW_IMAGE_URL = 'showImageUrl'

MANDATORY_FIELDS_OK_PARSER = [CHANNEL_NAME, OPEN_DATA_URL, \
                              SHOW_OBJECT_URL, SHOW_IMAGE_URL]

class OKImportParser():

    @staticmethod
    def parsePostParameters():
        args = loads(request.data)
        for key in MANDATORY_FIELDS_OK_PARSER:
            if key not in args:
                raise ValueError('{0} parameter is missing'.format(key))
            elif type(args[key]) is not unicode:
                raise ValueError('{0} value is not unicode'.format(key)) 
 
        return args
