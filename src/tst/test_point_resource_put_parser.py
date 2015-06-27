#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from flask import Flask, request
from werkzeug.exceptions import BadRequest
import sys
sys.path.append('../')
import service_resource
from json import dumps
from channel_parsers import ChannelResourceParser

URL = '/testservice/point/552833515c0dd1178d37f7bb/'
BAD_URL = '/testservice/point/11111111111dd1178d37f7bb/'
NAME = 'point_GT_1318'
JSON = "{'1': 'a', '2': 'b'}"

_JSON = 'json'
_NAME = 'name'
CORRECT_ARGS = {_NAME: NAME, _JSON: JSON}

app = Flask(__name__)

class test_GT_1318_Point_Parser(TestCase):
    def test_GT_1318_Point_Parser(self):
        
        with app.test_request_context(URL, data=CORRECT_ARGS, method='PUT'):
            args = ChannelResourceParser.parsePutParameters()
            self.assertEqual(args[_NAME], NAME)
            self.assertEqual(args[_JSON], JSON)

        with app.test_request_context(BAD_URL, data=CORRECT_ARGS, method='PUT'):
            with self.assertRaises(BadRequest):
                args = ChannelResourceParser.parsePutParameters()