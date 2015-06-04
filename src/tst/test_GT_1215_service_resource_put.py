#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from flask import Flask, request
from werkzeug.exceptions import BadRequest
import sys
sys.path.append('../')
import service_resource
from json import dumps

LOG_SIZE = 'logSize'
LOG_SIZE_VALUE = 10

CORRECT_ARGS = {LOG_SIZE: LOG_SIZE_VALUE}
INCORRECT_ARGS = {}

app = Flask(__name__)

class test_GT_1215ServiceResourcePut(TestCase):
    def test_GT_1215ServiceResourcePutFunc(self):

        with app.test_request_context('/testservice', data=CORRECT_ARGS, method='PUT'):
            args = service_resource.parsePut()
            self.assertEquals(args[LOG_SIZE], LOG_SIZE_VALUE)

        with app.test_request_context('/testservice', data=INCORRECT_ARGS, method='PUT'):
            with self.assertRaises(BadRequest):
                args = service_resource.parsePut()
