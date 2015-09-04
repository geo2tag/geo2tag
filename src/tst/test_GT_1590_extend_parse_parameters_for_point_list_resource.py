from unittest import TestCase
from flask import Flask
import sys
sys.path.append('../')
from point_list_resource_parser import PointListResourceParser

NO_BC_ERR_DATA = {
    'number': '10',
    'channel_ids': '556721a52a2e7febd2744201',
    'date_from': '1970-09-10T01:01:01.000000',
    'date_to': '2100-09-10T01:01:01.000000'
}

NO_BC_TO_ERR_DATA = NO_BC_ERR_DATA.copy()
NO_BC_TO_ERR_DATA['bc_from'] = 'true'

NO_BC_FROM_ERR_DATA = NO_BC_ERR_DATA.copy()
NO_BC_FROM_ERR_DATA['bc_to'] = 'true'

DATE_AND_BC_FLAGS = NO_BC_ERR_DATA.copy()
DATE_AND_BC_FLAGS['bc_from'] = 'true'
DATE_AND_BC_FLAGS['bc_to'] = 'true'

BC_FROM = 'bc_from'
BC_TO = 'bc_to'

BC_DATES_FLAG_CHECK_ARGS_KEY = 'args'
BC_DATES_FLAG_CHECK_ERR_KEY = 'err'

app = Flask(__name__)


class TestExtendPointListParserWithFlagsBC(TestCase):
    def testExtendPointListParserWithFlagsBC_DATES_NO_BC(self):
        with app.test_request_context(data=NO_BC_ERR_DATA):
            res = PointListResourceParser.parseGetParameters()
            self.assertEqual(res[BC_DATES_FLAG_CHECK_ARGS_KEY][BC_TO], None)
            self.assertEqual(res[BC_DATES_FLAG_CHECK_ARGS_KEY][BC_FROM], None)

    def testExtendPointListParserWithFlagsBC_DATES_NO_BC_TO(self):
        with app.test_request_context(data=NO_BC_TO_ERR_DATA):
            res = PointListResourceParser.parseGetParameters()
            self.assertEqual(res[BC_DATES_FLAG_CHECK_ARGS_KEY][BC_TO], None)
            self.assertEqual(res[BC_DATES_FLAG_CHECK_ARGS_KEY][BC_FROM], True)

    def testExtendPointListParserWithFlagsBC_DATES_NO_BC_FROM(self):
        with app.test_request_context(data=NO_BC_FROM_ERR_DATA):
            res = PointListResourceParser.parseGetParameters()
            self.assertEqual(res[BC_DATES_FLAG_CHECK_ARGS_KEY][BC_TO], True)
            self.assertEqual(res[BC_DATES_FLAG_CHECK_ARGS_KEY][BC_FROM], None)

    def testExtendPointListParserWithFlagsBC_DATES_BC_FROM_BC_TO(self):
        with app.test_request_context(data=DATE_AND_BC_FLAGS):
            res = PointListResourceParser.parseGetParameters()
            self.assertEqual(res[BC_DATES_FLAG_CHECK_ARGS_KEY][BC_TO], True)
            self.assertEqual(res[BC_DATES_FLAG_CHECK_ARGS_KEY][BC_FROM], True)



