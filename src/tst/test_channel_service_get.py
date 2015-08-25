#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from flask import Flask, request
import sys
sys.path.append('../')
from channels_list_parsers import ChannelsListResourceParser

NUMBER = 'number'
NUMBER_VALUE = 2
SUBSTRING = 'substring'
SUBSTRING_VALUE = u'тест'
OFFSET = 'offset'
OFFSET_VALUE = 3
CORRECT_ARGS = {
    NUMBER: NUMBER_VALUE,
    SUBSTRING: SUBSTRING_VALUE,
    OFFSET: OFFSET_VALUE}
BAD_REQUEST = {SUBSTRING: None, NUMBER: None, OFFSET: None}
URL = '/testservice/channel/'
BAD_URL = '/testservice/channel/?substring=тест&number=2&offset=3'
app = Flask(__name__)


class test_GT_1262ChannelServiceGet(TestCase):

    def test_GT_1262ChannelServiceGetFunc(self):

        with app.test_request_context(URL, method='GET'):
            args = ChannelsListResourceParser.parseGetParameters()
            self.assertEquals(args, BAD_REQUEST)

        with app.test_request_context(BAD_URL, method='GET'):
            args = ChannelsListResourceParser.parseGetParameters()
            self.assertEquals(args, CORRECT_ARGS)
