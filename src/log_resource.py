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
DATE_FROM = 'date_from'
DATE_TO = 'date_to'


class LogResource(Resource):
    def get(self, serviceName = None):
        parser_dict = LogParser.parseGetParameters()
        if serviceName == None:
            serviceName = getDbName()

        return getLog(serviceName, parser_dict[NUMBER], parser_dict[OFFSET], 
            parser_dict[DATE_FROM], parser_dict[DATE_TO])

def datetimeSerialiser(obj):
    if isinstance(obj, datetime) :
        return obj.isoformat()
    raise TypeError("%r is not JSON serializable" % obj)

def datetimeDeserialiser(dict):
    if "date" in dict :
        try :
            date = datetime.strptime(str(dict["date"]), "%Y-%m-%dT%H:%M:%S")
            return date
        except  ValueError:
            print "Non ISO8601 format"
            raise
    return dict

def datetime_from_iso8601(datetime_str):
    obj = datetime_str.replace("'", "").replace("\"", "")
    print obj
    try :
        return json.dumps(aniso8601.parse_datetime(obj), default = datetimeSerialiser)
    except  ValueError :
        raise
    return None
