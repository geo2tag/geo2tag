from db_model import getLog
from config_reader import getDbName
from flask import request
from flask.ext.restful import Resource
from flask_restful import reqparse
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
            dateDeserialiser(parser_dict, DATE_FROM), dateDeserialiser(parser_dict, DATE_TO))

def dateSerialiser(obj):
    if isinstance(obj, datetime) :
        return obj.isoformat()
    raise TypeError("%r is not JSON serializable" % obj)
def dateDeserialiser(dict, param_date):
    try :
        if param_date in dict and dict[param_date] != None :
            obj = dict[param_date].replace("'", "").replace("\"", "")
            return datetime.strptime(str(obj), ISO8601_FMT)
    except  ValueError:
        print "Non ISO8601 format"
        raise
    return None

def datetime_from_iso8601(datetime_str):
    try :
        obj = datetime_str.replace("'", "").replace("\"", "")
        return json.dumps(aniso8601.parse_datetime(obj), default = dateSerialiser)
    except  ValueError :
        raise
    return None
