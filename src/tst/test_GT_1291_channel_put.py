#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from flask import Flask, request
from werkzeug.exceptions import BadRequest
import service_resource
from json import dumps
from channel_parsers import ChannelResourceParser

URL = '/testservice/channel/channel_id/'
NAME = u'тестовое_имя'
JSON = u"{'число1':число2}"
ACL = 10

_NAME = 'name'
_JSON = 'json'
_ACL = 'acl'
CORRECT_ARGS = {_NAME: NAME, _JSON: JSON, _ACL: ACL}
INCORRECT_ARGS = {}

app = Flask(__name__)


class test_GT_1291_Channel_Parser(TestCase):

    def test_GT_1291_Channel_Parser(self):

        with app.test_request_context(URL, data=CORRECT_ARGS, method='PUT'):
            args = ChannelResourceParser.parsePutParameters()
            self.assertEqual(args[_NAME], NAME)
            self.assertEqual(args[_JSON], JSON)
            self.assertEqual(args[_ACL], ACL)

        with app.test_request_context(URL, data=INCORRECT_ARGS, method='PUT'):
            with self.assertRaises(BadRequest):
                args = ChannelResourceParser.parsePutParameters()
