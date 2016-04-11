from flask_restful import reqparse

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
BC = 'bc'
BC_FROM = 'bc_from'
BC_TO = 'bc_to'
LATITUDE = 'latitude'
LONGITUDE = 'longitude'
ZOOM = 'zoom'


class MapParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(CHANNEL_IDS, type=unicode)
        parser.add_argument(NUMBER, type=int)
        parser.add_argument(GEOMETRY, type=geo_json_type.GeoJsonType)
        parser.add_argument(ALTITUDE_FROM, type=float)
        parser.add_argument(ALTITUDE_TO, type=float)
        parser.add_argument(SUBSTRING, type=unicode)
        parser.add_argument(DATE_FROM, type=datetime_from_iso8601)
        parser.add_argument(DATE_TO, type=datetime_from_iso8601)
        parser.add_argument(OFFSET, type=int)
        parser.add_argument(RADIUS, type=float)
        parser.add_argument(BC_FROM, type=inputs.boolean)
        parser.add_argument(BC_TO, type=inputs.boolean)
        parser.add_argument(LATITUDE, type=float)
        parser.add_argument(LONGITUDE, type=float)
        parser.add_argument(ZOOM, type=int)
        args = parser.parse_args()
        return args
