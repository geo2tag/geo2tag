from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
from pymongo import MongoClient
from datetime import datetime
from calendar import timegm
import pymongo
import json
import aniso8601
import pytz

ISO8601_FMT = '%Y-%m-%dT%H:%M:%S'

NUMBER = 'number'
OFFSET = 'offset'
DATE_FROM = 'date_from'
DATE_TO = 'date_to'


class LogResource(Resource):
    def get(self, serviceName):
        parser_dict = parse()
        return {serviceName: 'Service description'}

    def put(self, serviceName):
        parser_dict = parse()
        return {serviceName: 'Service updated'}

    def delete(self, serviceName):
        parser_dict = parse()
        return {serviceName: 'Service removed'} 

def datetimeSerialiser(obj):
    if isinstance(obj, datetime):
        return obj.strftime(ISO8601_FMT)
    raise TypeError


def datetimeDeserialiser(dict):
    for key, value in dict.iteritems():
        if value == '':
            dict[key] = u''
            continue
        try:
            datetime_obj = datetime.datetime.strptime(value, ISO8601_FMT)
            dict[key] = datetime_obj
        except (ValueError, TypeError):
            continue
    return dict

def datetime_from_iso8601(datetime_str):
    return json.dumps(datetime.fromtimestamp(timegm(aniso8601.parse_datetime(datetime_str).utctimetuple()), tz=pytz.UTC), default = datetimeSerialiser)
def parse():
    parser = reqparse.RequestParser()
    parser.add_argument(NUMBER, type=int, default=None)
    parser.add_argument(OFFSET, type=int, default=None)
    parser.add_argument(DATE_FROM, type=datetime_from_iso8601, default=None)
    parser.add_argument(DATE_TO, type=datetime_from_iso8601, default=None)
    args = parser.parse_args()
    return args

 
