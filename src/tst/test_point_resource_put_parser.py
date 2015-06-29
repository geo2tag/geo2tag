#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from flask import Flask, request
from werkzeug.exceptions import BadRequest
import urllib2
import sys
sys.path.append('../')
import service_resource
from json import dumps
from point_resource_parsers import PointResourceParsers
from point_does_not_exist import PointDoesNotExist

URL = '/testservice/point/552833515c0dd1178d37f7bb/'
BAD_URL = '/testservice/point/552833515c0dd1178d37f7bb/'
LAT = 55.24
LAT_STR = '55.334'
JSON = "{'1': 'a', '2': 'b'}"
JSON_INT = 13
_ALT_LIST = [1,2,3,4,5,5]
_LAT = 'lat'
_LON = 'lon'
_ALT = 'alt'
_JSON = 'json'
_CHANNEL_ID = 'channel_id'
CORRECT_ARGS = {_LAT: LAT, _JSON: JSON}
INCORRECT_ARGS = {_LAT: LAT_STR, _JSON: JSON_INT, _ALT: _ALT_LIST}

app = Flask(__name__)

class test_GT_1318_Point_Parser(TestCase):
    def test_GT_1318_Point_Parser(self):

        with app.test_request_context(BAD_URL, data=INCORRECT_ARGS, method='PUT'):
            with self.assertRaises(ValueError):
                args = PointResourceParsers.parsePutParameters()
                print args, '22222222222'

        with app.test_request_context(URL, data=CORRECT_ARGS, method='PUT'):
            args = PointResourceParsers.parsePutParameters()
            self.assertEqual(args[_LAT], LAT)
            self.assertEqual(args[_JSON], JSON)