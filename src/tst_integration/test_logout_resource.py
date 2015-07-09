import unittest
import requests

from basic_integration_test import BasicIntegrationTest

from config_reader import getInstancePrefix

VALID_RESPONSE_CODE = 200
INVALID_RESPONSE_CODE = 400

TEST_ID = 'test_id'
GOOD_USER_ID_FIELD = 'user_id'
WRONG_USER_ID_FIELD = 'wrong_user_id'

LOGOUT_REQUEST_CONTEXT = '/' + getInstancePrefix() + "/logout"
GOOD_REQUEST_PARAM = "?" + GOOD_USER_ID_FIELD + "=" + TEST_ID
WRONG_REQUEST_PARAM = "?" + WRONG_USER_ID_FIELD + "=" + TEST_ID

class TestLogoutResource(BasicIntegrationTest) :
	def testLogoutResource(self) :
		response = requests.get(self.getUrl(LOGOUT_REQUEST_CONTEXT + GOOD_REQUEST_PARAM))
		self.assertEqual(response.status_code, VALID_RESPONSE_CODE)
		response = requests.get(self.getUrl(LOGOUT_REQUEST_CONTEXT + WRONG_REQUEST_PARAM))
		self.assertEqual(response.status_code, INVALID_RESPONSE_CODE)
		response = requests.get(self.getUrl(LOGOUT_REQUEST_CONTEXT))
		self.assertEqual(response.status_code, INVALID_RESPONSE_CODE)
