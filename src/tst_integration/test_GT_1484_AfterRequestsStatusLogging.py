from pymongo import DESCENDING
import requests
from basic_integration_test import BasicIntegrationTest
import sys

sys.path.append('../')
from config_reader import getInstancePrefix
from db_model import getDbObject

URL = '/' + getInstancePrefix() + '/status'

LOG = 'log'
ID = '_id'

log = getDbObject()[LOG]

MESSAGE_FIELD = 'message'
MESSAGE = 'Status_code: 200, response: [\'OK\']'


class TestAfterRequestStatusLogging(BasicIntegrationTest):

    def testAfterRequestStatusLogging(self):
        r = requests.get(self.getUrl(URL))
        last_doc = log.find().sort(ID, DESCENDING).limit(1)
        self.assertEqual(list(last_doc)[0][MESSAGE_FIELD], MESSAGE)
