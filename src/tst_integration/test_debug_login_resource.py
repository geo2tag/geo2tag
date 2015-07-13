import unittest
import requests
from basic_integration_test import BasicIntegrationTest
from flask import Flask, request
from debug_login_resource import DebugLoginResource

CORRECT_USER = 'debug_user1'
INCORRECT_USER = 'incorrectUser'
CORRECT_ARGS = {'_id':CORRECT_USER}
INCORRECT_ARGS = {'_id':INCORRECT_USER}

app = Flask(__name__)

class TestDebugLoginResource(BasicIntegrationTest):
    def testDebugLoginResource(self):

        with app.test_request_context(data=INCORRECT_ARGS, method = 'GET'):
        	self.assertRaises(BadRequest)
        
