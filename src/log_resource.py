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
from date_utils import dateSerialiser, dateDeserialiser, datetime_from_iso8601


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