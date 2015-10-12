from unittest import TestCase
from flask import request
from flask import Flask
from werkzeug.exceptions import BadRequest
from json import dumps
from geocoding_parser import GeocodingParser

app = Flask(__name__)

METHOD = 'POST'
DATA_ARR = ['channelName']
TEST_VAL_PREFIX = 'test_val_'
DATA = {
    DATA_ARR[0]: TEST_VAL_PREFIX + DATA_ARR[0],
}
INCORRECT_DATA = {
    DATA_ARR[0]: 123456,
}


class TestGeocodingParser(TestCase):

    def testGecodingParserPostDone(self):
        with app.test_request_context(data=dumps(DATA), method=METHOD):
            args = GeocodingParser.parsePostParameters()
            for el in DATA_ARR:
                self.assertEqual(args[el], TEST_VAL_PREFIX + el)

    def testGecodingParserPostFail(self):
        with app.test_request_context(data=dumps(INCORRECT_DATA), method=METHOD):
            with self.assertRaises(BadRequest):
                args = GeocodingParser.parsePostParameters()
