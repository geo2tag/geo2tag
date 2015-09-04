from unittest import TestCase
from flask import Flask, request
import ast
import sys
sys.path.append('../')
from point_list_resource import PointListResource

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

BC_FROM = '[bc_from] '
BC_TO = '[bc_to] '

ERR_MSG_KEY = 'message'
ERR_MSG = ': Missing required parameter in the JSON body or the post body or the query string'

NO_BC_ERR_DATA_RESP_TEXT = {ERR_MSG_KEY: BC_FROM + BC_TO + ERR_MSG}
NO_BC_TO_ERR_DATA_RESP_TEXT = {ERR_MSG_KEY: BC_TO + ERR_MSG}
NO_BC_FROM_ERR_DATA_RESP_TEXT = {ERR_MSG_KEY: BC_FROM + ERR_MSG}

app = Flask(__name__)


class TestExtendPointListParserWithFlagsBC(TestCase):


   def testExtendPointListParserWithFlagsBC_DATES_NO_BC(self):
       with app.test_request_context(data=NO_BC_ERR_DATA):
           self.assertEqual(PointListResource().get('geomongo')[0], NO_BC_ERR_DATA_RESP_TEXT)


   def testExtendPointListParserWithFlagsBC_DATES_NO_BC_TO(self):
       with app.test_request_context('/', data=NO_BC_TO_ERR_DATA):
           self.assertEqual(PointListResource().get('geomongo')[0], NO_BC_TO_ERR_DATA_RESP_TEXT)


   def testExtendPointListParserWithFlagsBC_DATES_NO_BC_FROM(self):
       with app.test_request_context('/', data=NO_BC_FROM_ERR_DATA):
           self.assertEqual(PointListResource().get('geomongo')[0], NO_BC_FROM_ERR_DATA_RESP_TEXT)
