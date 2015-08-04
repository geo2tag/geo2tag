import requests
import sys
import pymongo
from datetime import datetime
from basic_integration_test import BasicIntegrationTest
sys.path.append('../')
from db_model import getDbObject, getDbName
from url_routines import getInstancePrefix

COLLECTION_LOG = 'log'
collection_log = getDbObject(getDbName())[COLLECTION_LOG]

URL_STATUS = '/' + getInstancePrefix() + '/status'
ID = '_id'
MESSAGE_FIELD = 'message'
VALID_MESSAGE = 'Request url: http://geomongo/instance/status, request data: '

class TestAfterRequestWriteInstanceLog(BasicIntegrationTest):
    def testAfterRequestWriteInstanceLog(self):
        requests.get(self.getUrl(URL_STATUS))
        last_document = list(collection_log.find().sort(ID, pymongo.DESCENDING).limit(1))
        self.assertEqual(last_document[0][MESSAGE_FIELD], VALID_MESSAGE)