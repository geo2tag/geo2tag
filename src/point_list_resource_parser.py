from flask_restful import reqparse

CHANNELS_IDS = 'channel_ids'
NUMBER = 'number'
GEOMETRY = 'geometry'
ALTITUDE_FROM = 'altitude_from'
ALTITUDE_TO = 'altitude_to'
SUBSTRING = 'substring'
DATE_FROM = 'date_from'
DATE_TO = 'date_to'
OFFSET = 'offset'
RADIUS = 'radius'

class PointListResourceParser():
    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(CHANNELS_IDS, type=list, required=True)
        parser.add_argument(NUMBER, type=int, required=True)
        parser.add_argument(GEOMETRY, type=str)
        parser.add_argument(ALTITUDE_FROM, type=float)
        parser.add_argument(ALTITUDE_TO, type=float)
        parser.add_argument(SUBSTRING, type=str)
        parser.add_argument(DATE_FROM, type=int)
        parser.add_argument(DATE_TO, type=int)
        parser.add_argument(OFFSET, type=int)
        parser.add_argument(RADIUS, type=float, default=1000)
        args = parser.parse_args()
        return args