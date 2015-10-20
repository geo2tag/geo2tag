import pymongo
import unittest
from flask import session
from os import urandom
from flask import Flask, request, session
from db_model import getDbObject
from user_routines import logUserIn, logUserOut
from config_reader import getInstancePrefix


NAME_DB = "geomongo"
COLLECTION_NAME_LOG = "log"
COLLECTION_LOG = getDbObject(NAME_DB)[COLLECTION_NAME_LOG]

MESSAGE = 'message'
MSG_LOGIN = 'login'
MSG_LOGOUT = 'logout'
TEST_ID = 'test_id'

USER_ID_FIELD = 'user_id'
MSG_FIELD = 'message'

LOGOIN_REQUEST_CONTEXT = '/' + getInstancePrefix() + "/login"
LOGOUT_REQUEST_CONTEXT = '/' + getInstancePrefix() + "/logout"
REQUEST_PARAM = "?user_id=" + TEST_ID

app = Flask(__name__)
app.secret_key = urandom(32)


class TestUserRoutines(unittest.TestCase):

    def testUserRoutins(self):
        # Emulating login session
        with app.test_request_context(
                LOGOIN_REQUEST_CONTEXT + REQUEST_PARAM):
            logUserIn(request.args[USER_ID_FIELD])
            self.assertTrue(session[USER_ID_FIELD] == TEST_ID)
            # Testing writing in log
            IS_USER_LOGIN = COLLECTION_LOG.find(
                {
                    USER_ID_FIELD: TEST_ID,
                    MESSAGE: MSG_LOGIN}, None, 0, 1
            ).sort("_id", pymongo.DESCENDING)
            self.assertTrue(IS_USER_LOGIN.count() > 0)
            self.assertTrue(list(IS_USER_LOGIN)[0][MESSAGE] == MSG_LOGIN)
            # Emulating logout session
            logUserOut()
            self.assertTrue(USER_ID_FIELD not in session)
            # Testing writing in log
            IS_USER_LOGOUT = COLLECTION_LOG.find(
                {
                    USER_ID_FIELD: TEST_ID,
                    MESSAGE: MSG_LOGOUT}, None, 0, 1
            ).sort("_id", pymongo.DESCENDING)
            self.assertTrue(IS_USER_LOGOUT.count() > 0)
            self.assertTrue(list(IS_USER_LOGOUT)[0][MESSAGE] == MSG_LOGOUT)
