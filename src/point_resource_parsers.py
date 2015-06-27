from flask_restful import reqparse

LAT = 'lat'
LON = 'lon'
ALT = 'alt'
JSON = 'json'
CHANNEL_ID = 'channel_id'

class PointResourceParsers():
	@staticmethod
	def parsePutParameters():
		parser = reqparse.RequestParser()
        parser.add_argument(LAT, type=float)
        parser.add_argument(LON, type=float)
        parser.add_argument(ALT, type=float)
        parser.add_argument(JSON, type=str)
        parser.add_argument(CHANNEL_ID, type=str)
        args = parser.parse_args()
        return args