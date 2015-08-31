#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from flask import Flask, request

import sys
sys.path.append('../')
import service_list_resource
import service_resource
from json import dumps
from service_list_parsers import ServiceListParser

NUMBER = 'number'
NUMBER_VALUE = 0
OFFSET = 'offset'
OFFSET_VALUE = 0
CORRECT_ARGS = NUMBER + '=' + \
    str(NUMBER_VALUE) + '&' + OFFSET + '=' + str(OFFSET_VALUE)
INCORRECT_ARGS = 'incorrect_key='


NAME = 'name'
LOG_SIZE = 'logSize'
OWNER_ID = 'ownerId'

NAME_VALUE = u'имя'
LOG_SIZE_VALUE = 10
OWNER_ID_VALUE = u'индификатор_владельца'

DEFAULT_LOG_SIZE = 1048576
DEFAULT_OWNER_ID = 'STUB'
CORRECT_FORM = {
    NAME: NAME_VALUE,
    LOG_SIZE: LOG_SIZE_VALUE,
    OWNER_ID: OWNER_ID_VALUE}
SEMIFILLED_FORM = {NAME: NAME_VALUE}
INCORRECT_FORM = {}

app = Flask(__name__)


class TestParserServiceList(TestCase):

    def testGetParser(self):
        with app.test_request_context('/?' + CORRECT_ARGS):
            args = ServiceListParser.parseGetParameters()
            self.assertEquals(args[OFFSET], OFFSET_VALUE)
            self.assertEquals(args[NUMBER], NUMBER_VALUE)

        with app.test_request_context('/?' + INCORRECT_ARGS):
            args = ServiceListParser.parseGetParameters()
            self.assertIsNone(args.get(OFFSET))
            self.assertIsNone(args.get(NUMBER))

    def testPostParser(self):
        with app.test_request_context('/', data=CORRECT_FORM, method='POST'):
            args = ServiceListParser.parsePostParameters()
            self.assertEquals(args[NAME], NAME_VALUE)
            self.assertEquals(args[LOG_SIZE], LOG_SIZE_VALUE)
            self.assertEquals(args[OWNER_ID], OWNER_ID_VALUE)

        with app.test_request_context('/', data=SEMIFILLED_FORM, method='POST'):
            args = ServiceListParser.parsePostParameters()
            self.assertEquals(args[NAME], NAME_VALUE)
            self.assertEquals(args[LOG_SIZE], DEFAULT_LOG_SIZE)
            self.assertEquals(args[OWNER_ID], DEFAULT_OWNER_ID)
