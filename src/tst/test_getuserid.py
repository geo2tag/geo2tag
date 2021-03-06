from unittest import TestCase
from os import urandom
from flask import Flask, request
from user_routines import logUserIn, logUserOut, getUserId
from config_reader import getInstancePrefix


TEST_ID = 'test_id11'
USER_ID = 'user_id'
ANONYM = 'anonym'

LOGOIN_REQUEST_CONTEXT = '/' + getInstancePrefix() + "/login"
LOGOUT_REQUEST_CONTEXT = '/' + getInstancePrefix() + "/logout"
REQUEST_PARAM = "?user_id=" + TEST_ID

app = Flask(__name__)
app.secret_key = urandom(32)


class TestUserId(TestCase):

    def testUserId(self):
        with app.test_request_context(LOGOIN_REQUEST_CONTEXT + REQUEST_PARAM):
            # Emulating login session
            logUserIn(request.args[USER_ID])
            self.assertTrue(getUserId() == TEST_ID)
        # Emulating logout session
            logUserOut()
            self.assertTrue(getUserId() == ANONYM)
