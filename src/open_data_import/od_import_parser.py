from flask_restful import request
from json import loads
from werkzeug.exceptions import BadRequest
CHANNEL_NAME = 'channelName'
OPEN_DATA_URL = 'openDataUrl'
SHOW_OBJECT_URL = 'showObjectUrl'
SHOW_IMAGE_URL = 'showImageUrl'

MANDATORY_FIELDS_OK_PARSER = [CHANNEL_NAME, OPEN_DATA_URL]


class OdImportParser():

    @staticmethod
    def parsePostParameters():
        args = loads(request.get_data())
        for key in MANDATORY_FIELDS_OK_PARSER:
            if key not in args:
                raise BadRequest('{0} parameter is missing'.format(key))
            elif not isinstance(args[key], unicode):
                raise BadRequest('{0} value is not unicode'.format(key))

        return args
