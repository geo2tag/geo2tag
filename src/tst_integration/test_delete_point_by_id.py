import unittest
import requests
from pymongo import MongoClient
from basic_integration_test import BasicIntegrationTest
import sys
sys.path.append('../')
from db_model import getDbObject

TEST_SERVICE = 'testservice'
COLLECTION = 'points'
NAME = 'name'
NAME_TEST_OBJECT = 'test_GT_1307'
TEST_URL = '/instance/service/testservice/point/'
BAD_TEST_URL = '/instance/service/testservice/point/111117a47ec8115da7551111'
VALID_RESPONSE_CODE = 200
VALID_RESPONSE_TEXT = '{}'
NOT_VALID_RESPONSE_CODE = 404
NOT_VALID_RESPONSE_TEXT = "Point does not exist"

class TestPointResourceDelete(BasicIntegrationTest):
    def testPointResourceDelete(self):
        db = getDbObject(TEST_SERVICE)
        obj_id = db[COLLECTION].save({NAME: NAME_TEST_OBJECT})
        response = requests.delete(self.getUrl(TEST_URL + str(obj_id) + '/'))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.delete(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)