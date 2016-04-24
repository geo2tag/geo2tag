from flask_restful import reqparse

MARKER = 'marker'
RADIUS = 'radius'
CHANNEL_ID = 'channel_id'


class IconResourceParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(MARKER, type=unicode)
        parser.add_argument(RADIUS, type=int)
        parser.add_argument(CHANNEL_ID, type=unicode)
        args = parser.parse_args()
        return args
