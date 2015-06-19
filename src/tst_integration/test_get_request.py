from pymongo import MongoClient
import sys
import unittest
import requests
import pymongo
from basic_integration_test import BasicIntegrationTest

sys.path.append('../')
from db_model import addService, removeService
from config_reader import getHost, getPort, getDbName

TEST_URL = '/instance/service/'
VALID_RESPONSE_CODE = 404
VALID_RESPONSE_TEXT = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>\n'
NOT_VALID_RESPONSE_CODE = 404
BAD_RESULT = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>\n'

TEST_NAME = 'name_service_test_get'
TEST_OBJ = { "name" : TEST_NAME, "offset" : 12 }
TEST_PARAMETERS = {"offset" : 12}
BAD_TEST_PARAMETERS = {"offset" : "string"}

db = MongoClient(getHost(), getPort())[getDbName()]
COLLECTION = 'services'

class TestServiceListGetRequest(BasicIntegrationTest):
    def testServiceListGetRequest(self):
    	obj_id = db[COLLECTION].save(TEST_OBJ)
        response = requests.get(self.getUrl(TEST_URL), params = TEST_PARAMETERS)
        removeService(TEST_NAME)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(TEST_URL), params = BAD_TEST_PARAMETERS)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, BAD_RESULT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)