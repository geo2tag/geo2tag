import unittest
import requests
from basic_integration_test import BasicIntegrationTest
from flask import Flask, request
from debug_login_resource import DebugLoginResource

TEST_URL = '/instance/login/debug?_id=debug_user1'
BAD_TEST_URL = '/instance/login/debug?_id=wrongUser'
VALID_RESPONSE_CODE = 200
NOT_VALID_RESPONSE_CODE = 401
NOT_VALID_RESPONSE_TEXT = 'Credentials are incorrect'
class TestDebugLoginResource(BasicIntegrationTest):
    def testDebugLoginResource(self):
        response = requests.get(self.getUrl(TEST_URL))
        responseCode = response.status_code
        self.assertEquals(responseCode, VALID_RESPONSE_CODE)
        response = requests.get(self.getUrl(BAD_TEST_URL))
        responseText = response.text
        responseCode = response.status_code
        self.assertEquals(responseText, NOT_VALID_RESPONSE_TEXT)
        self.assertEquals(responseCode, NOT_VALID_RESPONSE_CODE)

        
        
