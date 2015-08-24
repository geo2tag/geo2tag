from flask_restful import reqparse
import geo_json_type
from flask import request
from date_utils import dateDeserialiser, datetime_from_iso8601

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
        parser.add_argument(CHANNEL_IDS, type=str,
                            required=True, action='append')
        parser.add_argument(NUMBER, type=int, required=True)
        parser.add_argument(GEOMETRY, type=geo_json_type.GeoJsonType)
        parser.add_argument(ALTITUDE_FROM, type=float)
        parser.add_argument(ALTITUDE_TO, type=float)
        parser.add_argument(SUBSTRING, type=str)
        parser.add_argument(DATE_FROM, type=datetime_from_iso8601)
        parser.add_argument(DATE_TO, type=datetime_from_iso8601)
        parser.add_argument(OFFSET, type=int)
        parser.add_argument(RADIUS, type=float, default=1000)
        args = parser.parse_args()
        return args

    @staticmethod
    def parsePostParameters():
        jsonData = request.get_json(force=True)
        print jsonData
        args = validatePointsList(jsonData)
        return args


def validatePointsList(json):
    if not isinstance(json, list):
        raise ValueError('Value is not a list')
    for obj in json:
        if not ('lon' in obj.keys() and 'lat' in obj.keys() and
                'alt' in obj.keys() and 'json' in obj.keys() and
                'channel_id' in obj.keys()):
            raise ValueError('Incorrect keys')
        else:
            if not (
                isinstance(
                    obj['lat'],
                    int) or isinstance(
                    obj['lat'],
                    float)):
                raise ValueError("'lat' - Incorrect type")
            if not (
                isinstance(
                    obj['lon'],
                    int) or isinstance(
                    obj['lon'],
                    float)):
                raise ValueError("'lon' - Incorrect type")
            if not (
                isinstance(
                    obj['alt'],
                    int) or isinstance(
                    obj['alt'],
                    float)):
                raise ValueError("'alt' - Incorrect type")
            if not isinstance(obj['json'], dict):
                raise ValueError("'json' - Incorrect type")
            if not (
                isinstance(
                    obj['channel_id'],
                    str) or isinstance(
                    obj['channel_id'],
                    unicode)):
                raise ValueError("'channel_id' - Incorrect type")
    return json
