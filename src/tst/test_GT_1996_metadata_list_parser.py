#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from flask import Flask
from metadata_list_resource_parser import MetadataListResourceParser
from werkzeug.exceptions import BadRequest


NUMBER = 'number'
NUMBER_VALUE = 0
OFFSET = 'offset'
OFFSET_VALUE = 0
JSON = 'json'
JSON_VALUE = '{"a":"1", "b":"2"}'

CORRECT_GET_ARGS = NUMBER + '=' + unicode(NUMBER_VALUE) + \
    '&' + OFFSET + '=' + unicode(OFFSET_VALUE) + \
    '&' + JSON + '=' + unicode(JSON_VALUE)
CORRECT_POST_ARGS = {JSON: unicode(JSON_VALUE)}
INCORRECT_GET_ARGS = 'incorrect='
INCORRECT_POST_ARGS = {}

URL = '/testservice/metadata'

app = Flask(__name__)


class TestParserMetadataListResource(TestCase):

    def testGetParserMetadataListResource(self):
        with app.test_request_context('/?' + CORRECT_GET_ARGS):
            args = MetadataListResourceParser.parseGetParameters()
            self.assertEquals(args[OFFSET], OFFSET_VALUE)
            self.assertEquals(args[NUMBER], NUMBER_VALUE)
            self.assertEquals(args[JSON], JSON_VALUE)

        with app.test_request_context('/?' + INCORRECT_GET_ARGS):
            with self.assertRaises(BadRequest):
                args = MetadataListResourceParser.parseGetParameters()
                self.assertIsNone(args.get(OFFSET))
                self.assertIsNone(args.get(NUMBER))
                self.assertIsNone(args.get(JSON))

    def testPostParserMetadataListResource(self):
        with app.test_request_context(URL, data=CORRECT_POST_ARGS, method='POST'):
            args = MetadataListResourceParser.parsePostParameters()
            self.assertEquals(args[JSON], JSON_VALUE)

        with app.test_request_context(URL, data=INCORRECT_POST_ARGS, method='POST'):
            with self.assertRaises(BadRequest):
                args = MetadataListResourceParser.parsePostParameters()
