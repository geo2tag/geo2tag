from unittest import TestCase
from datetime import datetime, date, time
from flask import Flask, request
from calendar import timegm
import json
import aniso8601
import pytz

import sys
sys.path.append('../')
import log_resource
from log_parsers import LogParser


NUMBER = 'number'
NUMBER_VALUE = 0
OFFSET = 'offset'
OFFSET_VALUE = 0
DATE_FROM = 'date_from'
DATE_FROM_VALUE = '1970-06-15T18:00:00'
DATE_TO = 'date_to'
DATE_TO_VALUE = '2015-06-15T17:00:00'


CORRECT_ARGS = NUMBER+'='+str(NUMBER_VALUE)+'&'+OFFSET+'='+str(OFFSET_VALUE)+'&'+DATE_FROM+'='+str(DATE_FROM_VALUE)+'&'+DATE_TO+'='+str(DATE_TO_VALUE)
INCORRECT_ARGS='incorect='
app = Flask(__name__)
class TestParserLogResource(TestCase):
    def testGetParser(self):
        with app.test_request_context('/?' + CORRECT_ARGS):
            args = LogParser.parseGetParameters()
            self.assertEquals(args[OFFSET], OFFSET_VALUE)
            self.assertEquals(args[NUMBER], NUMBER_VALUE)
            loadedDatetime_from = json.loads(args[DATE_FROM], object_hook = log_resource.dateDeserialiser(args,DATE_FROM))
            self.assertEquals(loadedDatetime_from, DATE_FROM_VALUE)
            loadedDatetime_to = json.loads(args[DATE_TO], object_hook = log_resource.dateDeserialiser(args,DATE_TO))
            self.assertEquals(loadedDatetime_to, DATE_TO_VALUE)

        with app.test_request_context('/?'+INCORRECT_ARGS):
            args = LogParser.parseGetParameters()
            self.assertIsNone(args.get(OFFSET))
            self.assertIsNone(args.get(NUMBER))
            self.assertIsNone(args.get(loadedDatetime_from))
            self.assertIsNone(args.get(loadedDatetime_to))