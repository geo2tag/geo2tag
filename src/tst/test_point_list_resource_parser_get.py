#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from flask import Flask
import json
from werkzeug.exceptions import BadRequest
from point_list_resource_parser import PointListResourceParser
import geo_json_type
from date_utils import dateDeserialiser


NUMBER = 'number'
NUMBER_VALUE = 0
OFFSET = 'offset'
OFFSET_VALUE = 0
DATE_FROM = 'date_from'
DATE_FROM_VALUE = '1970-06-15T18:00:00.000000'
BC_FROM = 'bc_from'
BC_FROM_VALUE = 'true'
DATE_TO = 'date_to'
DATE_TO_VALUE = '2015-06-15T17:00:00.000000'
BC_TO = 'bc_to'
BC_TO_VALUE = 'true'
CHANNEL_IDS = 'channel_ids'
CHANNEL_IDS_VALUE = u'канал_ид'
GEOMETRY = 'geometry'
GEOMETRY_VALUE = '{"coordinates": [-115.8, 37.2], "type": "Point"}'
GEOMETRY_VALUE_JSON = {"coordinates": [-115.8, 37.2], "type": "Point"}


CORRECT_ARGS = NUMBER + '=' + unicode(NUMBER_VALUE) + '&' + OFFSET + '=' + \
    unicode(OFFSET_VALUE) + '&' + DATE_FROM + '=' + \
    unicode(DATE_FROM_VALUE) + '&' + \
    DATE_TO + '=' + unicode(DATE_TO_VALUE) + '&' + \
    BC_FROM + '=' + BC_FROM_VALUE + \
    '&' + BC_TO + '=' + BC_TO_VALUE + '&' + CHANNEL_IDS + '=' + \
    CHANNEL_IDS_VALUE + '&' + GEOMETRY + '=' + GEOMETRY_VALUE
INCORRECT_ARGS = 'incorect='
app = Flask(__name__)


class TestParserPointListGetResource(TestCase):

    def testParserPointListGetResource(self):
        with app.test_request_context(
                '/instance/service/testservice/point/?' + CORRECT_ARGS):
            args = PointListResourceParser.parseGetParameters()
            self.assertEquals(args[OFFSET], OFFSET_VALUE)
            self.assertEquals(args[NUMBER], NUMBER_VALUE)
            loadedDatetime_from = json.loads(
                args[DATE_FROM], object_hook=dateDeserialiser(
                    args, args[DATE_FROM]))
            self.assertEquals(loadedDatetime_from, DATE_FROM_VALUE)
            loadedDatetime_to = json.loads(
                args[DATE_TO], object_hook=dateDeserialiser(
                    args, args[DATE_TO]))
            self.assertEquals(loadedDatetime_to, DATE_TO_VALUE)
            geometryValue = geo_json_type.GeoJsonType(
                unicode(args.get(GEOMETRY)))
            self.assertEquals(GEOMETRY_VALUE_JSON, geometryValue)

        with app.test_request_context(
                '/instance/service/testservice/point/?' + INCORRECT_ARGS):
            with self.assertRaises(BadRequest):
                args = PointListResourceParser.parseGetParameters()
