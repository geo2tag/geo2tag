from unittest import TestCase
from datetime import datetime, date, time
from flask import Flask, request
from calendar import timegm
import json
import aniso8601
import pytz
from werkzeug.exceptions import BadRequest
from geojson import MultiPoint

import sys
sys.path.append('../')
import log_resource
from point_list_resource_parser import PointListResourceParser


NUMBER = 'number'
NUMBER_VALUE = 0
OFFSET = 'offset'
OFFSET_VALUE = 0
DATE_FROM = 'date_from'
DATE_FROM_VALUE = '1970-06-15T18:00:00'
DATE_TO = 'date_to'
DATE_TO_VALUE = '2015-06-15T17:00:00'
CHANNEL_IDS = 'channel_ids'
CHANNEL_IDS_VALUE = 'channel_ids_value'
GEOMETRY = 'geometry'
GEOMETRY_VALUE_LIST = [(-155.52, 19.61), (-156.22, 20.74), (-157.97, 21.46)]
GEOMETRY_VALUE_STR = '[(-155.52, 19.61), (-156.22, 20.74), (-157.97, 21.46)]'

CORRECT_ARGS = NUMBER+'='+str(NUMBER_VALUE)+'&'+OFFSET+'='+str(OFFSET_VALUE)+'&'+DATE_FROM+'='+str(DATE_FROM_VALUE)+'&'+DATE_TO+'='+str(DATE_TO_VALUE)+'&'+CHANNEL_IDS+'='+CHANNEL_IDS_VALUE+'&'+GEOMETRY+'='+GEOMETRY_VALUE_STR
INCORRECT_ARGS='incorect='
app = Flask(__name__)
class TestParserPointListGetResource(TestCase):
    def testParserPointListGetResource(self):
        with app.test_request_context('/instance/service/testservice/point/?' + CORRECT_ARGS):
            args = PointListResourceParser.parseGetParameters()
            print args
            print CORRECT_ARGS
            self.assertEquals(args[OFFSET], OFFSET_VALUE)
            self.assertEquals(args[NUMBER], NUMBER_VALUE)
            loadedDatetime_from = json.loads(args[DATE_FROM], object_hook = log_resource.datetimeDeserialiser(args))
            self.assertEquals(loadedDatetime_from, DATE_FROM_VALUE)
            loadedDatetime_to = json.loads(args[DATE_TO], object_hook = log_resource.datetimeDeserialiser(args))
            self.assertEquals(loadedDatetime_to, DATE_TO_VALUE)


        with app.test_request_context('/instance/service/testservice/point/?'+INCORRECT_ARGS):
            with self.assertRaises(BadRequest):
                args = PointListResourceParser.parseGetParameters()