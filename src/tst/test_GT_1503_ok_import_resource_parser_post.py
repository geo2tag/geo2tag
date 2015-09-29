from unittest import TestCase
from flask import request
from flask import Flask
from werkzeug.exceptions import BadRequest
from json import dumps
from ok_import_resource_parser import OKImportParser

app = Flask(__name__)

METHOD = 'POST'
DATA_ARR = ['channelName', 'openDataUrl', 'showObjectUrl', 'showImageUrl']
TEST_VAL_PREFIX = 'test_val_'
DATA = {
    DATA_ARR[0]: TEST_VAL_PREFIX + DATA_ARR[0],
    DATA_ARR[1]: TEST_VAL_PREFIX + DATA_ARR[1],
    DATA_ARR[2]: TEST_VAL_PREFIX + DATA_ARR[2],
    DATA_ARR[3]: TEST_VAL_PREFIX + DATA_ARR[3]
}
INCORRECT_DATA = {
    DATA_ARR[0]: 123456,
    DATA_ARR[1]: TEST_VAL_PREFIX + DATA_ARR[1],
    DATA_ARR[3]: 123456
}


class TestOKImportParserPost(TestCase):

    def testOKImportParserPostDone(self):
        with app.test_request_context(data=dumps(DATA), method=METHOD):
            args = OKImportParser.parsePostParameters()
            for el in DATA_ARR:
                self.assertEqual(args[el], TEST_VAL_PREFIX + el)

    def testOKImportParserPostFail(self):
        with app.test_request_context(data=dumps(INCORRECT_DATA), method=METHOD):
            with self.assertRaises(BadRequest):
                args = OKImportParser.parsePostParameters()
