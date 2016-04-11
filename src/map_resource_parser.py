from flask_restful import reqparse

CHANNEL_IDS = 'channel_ids'


class MapParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(CHANNEL_IDS, type=unicode)
        args = parser.parse_args()
        return args
