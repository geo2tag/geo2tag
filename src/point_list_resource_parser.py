from flask_restful import reqparse, inputs
from bson.errors import InvalidId
from bson.objectid import ObjectId
import geo_json_type
from flask import request
from date_utils import datetime_from_iso8601
from decoding_of_the_json_data_failed_exception \
    import DecodingOfTheJsonDataFailedException
from value_json_exception import ValueJSONException


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

BC_DATES_FLAG_CHECK_ERR_KEY = 'err'


class PointListResourceParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(CHANNEL_IDS, type=unicode,
                            required=True, action='append')
        parser.add_argument(NUMBER, type=int, required=True)
        parser.add_argument(GEOMETRY, type=geo_json_type.GeoJsonType)
        parser.add_argument(ALTITUDE_FROM, type=float)
        parser.add_argument(ALTITUDE_TO, type=float)
        parser.add_argument(SUBSTRING, type=unicode)
        parser.add_argument(DATE_FROM, type=datetime_from_iso8601)
        parser.add_argument(DATE_TO, type=datetime_from_iso8601)
        parser.add_argument(OFFSET, type=int)
        parser.add_argument(RADIUS, type=float, default=1000)
        parser.add_argument(BC_FROM, type=inputs.boolean)
        parser.add_argument(BC_TO, type=inputs.boolean)
        parser.add_argument(LATITUDE, type=float)
        parser.add_argument(LONGITUDE, type=float)
        parser.add_argument(ZOOM, type=int, default=14)
        args = parser.parse_args()
        # Generating dict with error array for 'bc_from' and 'bc_to' parameters
        # if error appeared
        res = args
        res[BC_DATES_FLAG_CHECK_ERR_KEY] = []
        if args[DATE_FROM] is not None and args[BC_FROM] is None:
            res[BC_DATES_FLAG_CHECK_ERR_KEY].append(BC_FROM)
        if args[DATE_TO] is not None and args[BC_TO] is None:
            res[BC_DATES_FLAG_CHECK_ERR_KEY].append(BC_TO)

        return res

    @staticmethod
    def parsePostParameters():
        jsonData = request.get_json(force=True, silent=True)
        if jsonData is None:
            raise DecodingOfTheJsonDataFailedException
        jsonData = validatePointsList(jsonData)
        args = parseBcParametr(jsonData)
        return args


def parseBcParametr(json):
    for obj in json:
        if not (BC in obj.keys()):
            obj[BC] = False
    return json


def validatePointsList(json):
    if not isinstance(json, list):
        raise ValueJSONException('Value is not a list')
    for obj in json:
        if not ('lon' in obj.keys() and 'lat' in obj.keys() and
                'alt' in obj.keys() and 'json' in obj.keys() and
                'channel_id' in obj.keys()):
            raise ValueJSONException('Incorrect keys')
        else:
            if not (
                isinstance(
                    obj['lat'],
                    int) or isinstance(
                    obj['lat'],
                    float)):
                raise ValueJSONException("'lat' - Incorrect type")
            if not (
                isinstance(
                    obj['lon'],
                    int) or isinstance(
                    obj['lon'],
                    float)):
                raise ValueJSONException("'lon' - Incorrect type")
            if not (
                isinstance(
                    obj['alt'],
                    int) or isinstance(
                    obj['alt'],
                    float)):
                raise ValueJSONException("'alt' - Incorrect type")
            if not isinstance(obj['json'], dict):
                raise ValueJSONException("'json' - Incorrect type")
            if not (
                isinstance(
                    obj['channel_id'],
                    str) or isinstance(
                    obj['channel_id'],
                    unicode)):
                raise ValueJSONException("'channel_id' - Incorrect type")
            if ('bc' in obj.keys() and not isinstance(obj['bc'], bool)):
                raise ValueJSONException("'bc' - Incorrect type")
            if obj['channel_id'] != '':
                try:
                    ObjectId(obj['channel_id'])
                except InvalidId:
                    raise ValueJSONException(
                        obj['channel_id'] + ' is not a valid ObjectId')
    return json
