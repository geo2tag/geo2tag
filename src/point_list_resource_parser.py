from flask_restful import reqparse
import log_resource
import geo_json_type

CHANNEL_IDS = 'channel_ids'
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
        parser.add_argument(CHANNEL_IDS, type=str, required=True)
        parser.add_argument(NUMBER, type=int, required=True)
        parser.add_argument(GEOMETRY, type=geo_json_type.GeoJsonType)
        parser.add_argument(ALTITUDE_FROM, type=float)
        parser.add_argument(ALTITUDE_TO, type=float)
        parser.add_argument(SUBSTRING, type=str)
        parser.add_argument(DATE_FROM, type=log_resource.datetime_from_iso8601)
        parser.add_argument(DATE_TO, type=log_resource.datetime_from_iso8601)
        parser.add_argument(OFFSET, type=int)
        parser.add_argument(RADIUS, type=float, default=1000)
        args = parser.parse_args()
        return args
