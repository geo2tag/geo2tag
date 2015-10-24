#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from flask import Flask
from werkzeug.exceptions import BadRequest
from channels_list_parsers import ChannelsListResourceParser

URL = '/testservice/channel/'
NAME = u'тестовое_имя'
JSON = u"{'число1':число2}"

CORRECT_ARGS = {'name': NAME, 'json': JSON}
INCORRECT_ARGS = {}

app = Flask(__name__)


class test_GT_1281ChannelsListResourceParser(TestCase):

    def test_GT_1281ChannelsListResourceParserFunc(self):

        with app.test_request_context(URL, data=CORRECT_ARGS, method='POST'):
            args = ChannelsListResourceParser.parsePostParameters()
            self.assertEquals(args['name'], NAME)
            self.assertEquals(args['json'], JSON)

        with app.test_request_context(URL, data=INCORRECT_ARGS, method='POST'):
            with self.assertRaises(BadRequest):
                args = ChannelsListResourceParser.parsePostParameters()
