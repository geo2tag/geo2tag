from flask_restful import reqparse
from datetime import datetime, date, time
from calendar import timegm
import date_utils
import pymongo
import json
import aniso8601
import pytz
NUMBER = "number"
OFFSET = "offset"
DATE_FROM = 'date_from'
DATE_TO = 'date_to'


class LogParser():

    @staticmethod
    def parseGetParameters():
        parser = reqparse.RequestParser()
        parser.add_argument(NUMBER, type=int, default=None)
        parser.add_argument(OFFSET, type=int, default=None)
        parser.add_argument(
            DATE_FROM, type=date_utils.datetime_from_iso8601, default=None)
        parser.add_argument(
            DATE_TO, type=date_utils.datetime_from_iso8601, default=None)
        args = parser.parse_args()
        return args
