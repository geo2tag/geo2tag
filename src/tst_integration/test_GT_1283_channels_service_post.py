import sys
import unittest
import requests
from basic_integration_test import BasicIntegrationTest
import json
from bson.objectid import ObjectId
sys.path.append('../')
from db_model import getDbObject
from config_reader import getHost, getPort
TEST_URL = '/instance/service/testservice/channel'

TEST_SERVICE = 'testservice'
NAME = 'tes t_name'
JSON = "{'1': 2, '2': '4'}"
JSON2 = [1, 2, 3]
DATA = {'name': NAME, 'json': JSON}
DATA2 = {'name': 123}


class TestChannelServicePostRequest(BasicIntegrationTest):

    def testChannelServicePostRequest(self):
        db = getDbObject(TEST_SERVICE)
        response = requests.post(self.getUrl(TEST_URL), data=DATA)
        responseText = response.text
        responseCode = response.status_code
        ID = json.loads(responseText)
        db['channels'].remove({'_id': ObjectId(ID['$oid'])})
        self.assertNotEquals(responseText, [])
        self.assertNotEquals(responseText, {})
        self.assertEquals(responseCode, 200)
        response = requests.post(self.getUrl(TEST_URL), data=DATA2)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseCode, 400)
