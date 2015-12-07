#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from flask import Flask
from werkzeug.exceptions import BadRequest
from metadata_resource_parser import MetadataParser

JSON = 'json'
JSON_VALUE = "{'a':'1', 'b':'2'}"

CORRECT_ARGS = {JSON: JSON_VALUE}
INCORRECT_ARGS = {}

URL = '/testservice/metadata'

app = Flask(__name__)


class TestMetadataResourceParser(TestCase):

    def testMetadataResourceParser(self):

        with app.test_request_context(URL, data=CORRECT_ARGS,
                                      method='PUT'):
            args = MetadataParser.parsePutParameters()
            self.assertEquals(args[JSON], JSON_VALUE)

        with app.test_request_context(URL, data=INCORRECT_ARGS,
                                      method='PUT'):
            with self.assertRaises(BadRequest):
                args = MetadataParser.parsePutParameters()
