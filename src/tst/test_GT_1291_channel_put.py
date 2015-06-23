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

URL = '/testservice/channel/channel_id/'
NAME = 'test_name'
JSON = "{'1':2}"
ACL = 10

CORRECT_ARGS = {'name': NAME, 'json': JSON, 'acl': ACL}
INCORRECT_ARGS = {}

app = Flask(__name__)

class test_GT_1291_Channel_Parser(TestCase):
    def test_GT_1291_Channel_Parser(self):
    	
        with app.test_request_context(URL, data=CORRECT_ARGS, method='PUT'):
            args = ChannelResourceParser.parsePutParameters()
            self.assertEqual(args['name'], 'test_name')
            self.assertEqual(args['json'], "{'1':2}")
            self.assertEqual(args['acl'], 10)

        with app.test_request_context(URL, data=INCORRECT_ARGS, method='PUT'):
            with self.assertRaises(BadRequest):
                args = ChannelResourceParser.parsePutParameters()