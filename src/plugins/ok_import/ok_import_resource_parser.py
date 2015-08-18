from flask_restful import reqparse

CHANNEL_NAME = 'channelName'
OPEN_DATA_URL = 'openDataUrl'
SHOW_OBJECT_URL = 'showObjectUrl'
SHOW_IMAGE_URL = 'showImageUrl'


class OKImportParser():

    @staticmethod
    def parsePostParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(CHANNEL_NAME, type=str, required=True)
        parser.add_argument(OPEN_DATA_URL, type=str, required=True)
        parser.add_argument(SHOW_OBJECT_URL, type=str, required=True)
        parser.add_argument(SHOW_IMAGE_URL, type=str, required=True)
        args = parser.parse_args()
        return args
