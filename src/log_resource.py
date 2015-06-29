from db_model import getLog
from config_reader import getDbName
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
from log_parsers import LogParser

ISO8601_FMT = '%Y-%m-%dT%H:%M:%S'

NUMBER = 'number'
OFFSET = 'offset'
DATE_FROM = 'dateFrom'
DATE_TO = 'dateTo'


class LogResource(Resource):
    def get(self, serviceName = None):
        parser_dict = parse()
        if serviceName == None:
            serviceName = getDbName()

        return getLog(serviceName, parser_dict[NUMBER], parser_dict[OFFSET], 
            parser_dict[DATE_FROM], parser_dict[DATE_TO])

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
            datetime_obj = datetime.strptime(value, ISO8601_FMT)
            dict[key] = datetime_obj
        except (ValueError, TypeError):
            continue
    return dict

def datetime_from_iso8601(datetime_str):
    return json.dumps(datetime.fromtimestamp(timegm(aniso8601.parse_datetime(datetime_str).utctimetuple()), tz=pytz.UTC), default = datetimeSerialiser)
