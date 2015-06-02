#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from flask import Flask, request, test_request_context

import sys
sys.path.append('../')
import service_list_resource 
import service_resource


NUMBER = 'number'
NUMBER_VALUE = 0
OFFSET = 'offset'
OFFSET_VALUE = 0
CORRECT_ARGS={NUMBER:NUMBER_VALUE, OFFSET:OFFSET_VALUE}
INCORRECT_ARGS={'incorrect_key':''}


NAME = 'name'
LOG_SIZE = 'log_size'
OWNER_ID = 'owner_id'

NAME_VALUE = 'nameval'
LOG_SIZE_VALUE = 10
OWNER_ID_VALUE = 'owneridval'

DEFAULT_LOG_SIZE = 1048576
DEFAULT_OWNER_ID = 'STUB'
CORRECT_FORM = {NAME: NAME_VALUE, LOG_SIZE: LOG_SIZE_VALUE, OWNER_ID: OWNER_ID_VALUE}
SEMIFILLED_FORM = {NAME: NAME_VALUE}
INCORRECT_FORM = {}

app = Flask(__name__)

class TestParserServiceList(TestCase):
    def testGetParser(self):
        with app.test_request_context('/', args=CORRECT_ARGS):
            args = service_list_resource.parser()
            self.assertEquals(args[OFFSET], OFFSET_VALUE)
            self.assertEquals(args[NUMBER], NUMBER_VALUE)

        with app.test_request_context('/', args=CORRECT_ARGS):
            args = service_list_resource.parser()
            self.assertIsNone(args.get(OFFSET))
            self.assertIsNone(args.get(NUMBER))

    def testPostParser(self):
        with app.test_request_context('/', form=CORRECT_FORM, method='POST'):
            args = service_resource.parse()
            self.assertEquals(args[NAME], NAME_VALUE)
            self.assertEquals(args[LOG_SIZE], LOG_SIZE_VALUE)
            self.assertEquals(args[OWNER_ID], OWNER_ID_VALUE)

        with app.test_request_context('/', form=SEMIFILLED_FORM, method='POST'):
            args = service_resource.parse()
            self.assertEquals(args[NAME], NAME_VALUE)
            self.assertEquals(args[LOG_SIZE], DEFAULT_LOG_SIZE)
            self.assertEquals(args[OWNER_ID], DEFAULT_OWNER_ID)

        with app.test_request_context('/', form=INCORRECT_FORM, method='POST'):
            args = service_resource.parse()

