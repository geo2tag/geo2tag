#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from debug_login_resource import parseId
from flask import Flask, request


USERNAME = 'abcd'
CORRECT_ARGS = {'_id':USERNAME}
INCORRECT_ARGS = {}

app = Flask(__name__)

class test_GT_1347_parser(TestCase):
    def test_GT_1347_parser(self):

        with app.test_request_context(data=CORRECT_ARGS):
            arr = parseId()
            self.assertEqual(arr['_id'], USERNAME)
        with app.test_request_context(data=INCORRECT_ARGS):
            arr = parseId()
            self.assertEqual(arr['_id'], None)


            