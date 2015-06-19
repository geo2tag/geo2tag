import sys
import unittest
import requests
from basic_integration_test import BasicIntegrationTest

sys.path.append("../")
from db_model import removeService
from  service_not_found_exception import ServiceNotFoundException

TEST_URL = '/instance/service/'
VALID_NAME = 'test_servise_post'
EXIST_NAME = 'testservice'
DATA = {'name': VALID_NAME}
DATA2 = {'name': EXIST_NAME}
VALID_RESPONSE_TEXT = {}
EXIST_RESPONSE_TEXT = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>\n'
VALID_RESPONSE_CODE = 404
NOT_VALID_RESPONSE_CODE = 404
class TestServiceListPostRequest(BasicIntegrationTest):
    def testServiceListPostRequest(self):
        response = requests.post(self.getUrl(TEST_URL), data = DATA)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(-1, responseText.find("$oid"))
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.post(self.getUrl(TEST_URL), data = DATA2)
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, EXIST_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)
        with self.assertRaises(ServiceNotFoundException) as e:
            removeService(VALID_NAME)