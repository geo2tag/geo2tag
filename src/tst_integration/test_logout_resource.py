import unittest
import requests

from basic_integration_test import BasicIntegrationTest

from config_reader import getInstancePrefix

VALID_RESPONSE_CODE = 200

LOGOUT_REQUEST_CONTEXT = '/' + getInstancePrefix() + "/logout"

class TestLogoutResource(BasicIntegrationTest) :
    def testLogoutResource(self) :
        response = requests.get(self.getUrl(LOGOUT_REQUEST_CONTEXT))
        self.assertEqual(response.status_code, VALID_RESPONSE_CODE)
