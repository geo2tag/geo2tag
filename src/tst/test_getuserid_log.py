from unittest import TestCase
from os import urandom
from flask import Flask, request
from user_routines import logUserIn, logUserOut, getUserId
from config_reader import getInstancePrefix
from db_model import getDbObject

MESSAGE = 'message'
COLLECTION_LOG_NAME = "log"
TEST_ID = 'test_id'
USER_ID = 'user_id'
ANONYM = 'anonym'
ANONYM_MESS = None
AUTH_MESS = 'login'

LOGOIN_REQUEST_CONTEXT = '/' + getInstancePrefix() + "/login"
LOGOUT_REQUEST_CONTEXT = '/' + getInstancePrefix() + "/logout"
REQUEST_PARAM = "?user_id=" + TEST_ID

app = Flask(__name__)
app.secret_key = urandom(32)


class TestUserIdLog(TestCase):

    def testUserIdLog(self):
        db = getDbObject()
        collection = db[COLLECTION_LOG_NAME]
        with app.test_request_context(LOGOIN_REQUEST_CONTEXT + REQUEST_PARAM):
            # Emulating login session
            collection.drop()
            logUserIn(request.args[USER_ID])
            getUserId()
            db_res = collection.find_one({USER_ID: TEST_ID})
            self.assertEqual(db_res[MESSAGE], AUTH_MESS)
        # Emulating logout session
            collection.drop()
            logUserOut()
            getUserId()
            db_res = collection.find_one({USER_ID: USER_ID})
            self.assertEqual(db_res, ANONYM_MESS)
