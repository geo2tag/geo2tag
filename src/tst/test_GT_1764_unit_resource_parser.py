#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from UserListResourceParser import Userlistresourceparser
from flask import Flask


NUMBER = 'number'
NUMBER_VALUE = 0
OFFSET = 'offset'
OFFSET_VALUE = 0
LOGIN = 'login'
LOGIN_VALUE = ''
CORRECT_ARGS = NUMBER + '=' + \
    str(NUMBER_VALUE) + '&' + OFFSET + '=' + str(OFFSET_VALUE) + \
    '&' + LOGIN + '=' + str(LOGIN_VALUE)
INCORRECT_ARGS = 'incorrect_key='

app = Flask(__name__)


class TestGt1764UnitResourceParser(TestCase):

    def testGetParser(self):
        with app.test_request_context('/?' + CORRECT_ARGS):
            args = Userlistresourceparser.parseGetParameters()
            self.assertEquals(args[LOGIN], LOGIN_VALUE)
            self.assertEquals(args[OFFSET], OFFSET_VALUE)
            self.assertEquals(args[NUMBER], NUMBER_VALUE)

        with app.test_request_context('/?' + INCORRECT_ARGS):
            args = Userlistresourceparser.parseGetParameters()
            self.assertIsNone(args.get(LOGIN))
            self.assertIsNone(args.get(OFFSET))
            self.assertIsNone(args.get(NUMBER))



