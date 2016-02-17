import pymongo
import unittest
from os import urandom
from flask import Flask, request, session
from db_model import getDbObject
from user_routines import logUserIn, logUserOut, findUsers
from config_reader import getInstancePrefix


NAME_DB = "geomongo"
COLLECTION_NAME_LOG = "log"
COLLECTION_NAME_USERS = "users"
COLLECTION_LOG = getDbObject(NAME_DB)[COLLECTION_NAME_LOG]
COLLECTION_USERS = getDbObject(NAME_DB)[COLLECTION_NAME_USERS]

MESSAGE = 'message'
MSG_LOGIN = 'login'
MSG_LOGOUT = 'logout'
TEST_ID = 'test_id'
TEST_LOGIN = 'test_login'

USER_ID_FIELD = 'user_id'
USER_LOGIN_FIELD = 'user_login'
MSG_FIELD = 'message'
LOGIN = u'login'

LOGOIN_REQUEST_CONTEXT = '/' + getInstancePrefix() + "/login"
LOGOUT_REQUEST_CONTEXT = '/' + getInstancePrefix() + "/logout"
REQUEST_PARAM = "?user_id=" + TEST_ID + '&user_login=' + TEST_LOGIN

TEST_NUMBER = 1
TEST_NUMBER_10 = 10
TEST_OFFSET = 0
TEST_LOGIN_SUBSTRING_TEST = u'test'
TEST_LOGIN_SUBSTRING = u'345'
TEST_OBJ = {'login': 'test_login_12345_qwerty'}
TEST_OBJ_1 = {'login': 'test_login_qwerty'}
TEST_OBJ_2 = {'login': 'test_login_333'}
TEST_OBJ_3 = {'login': 'test_login_222'}
TEST_OBJ_4 = {'login': 'test_login_111'}
VALID_RESULT = u'test_login_12345_qwerty'

app = Flask(__name__)
app.secret_key = urandom(32)


def isSorted(L, key):
    tmp = L[0][key]
    for i in L:
        if i[key] < tmp:
            return False
        else:
            tmp = i[key]
    return True


class TestUserRoutines(unittest.TestCase):

    def testUserRoutins(self):
        # Emulating login session
        with app.test_request_context(
                LOGOIN_REQUEST_CONTEXT + REQUEST_PARAM):
            logUserIn(
                request.args[USER_ID_FIELD],
                request.args[USER_LOGIN_FIELD])
            self.assertTrue(session[USER_ID_FIELD] == TEST_ID)
            self.assertTrue(session[USER_LOGIN_FIELD] == TEST_LOGIN)
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

    def testFindUsers(self):
        COLLECTION_USERS.insert(TEST_OBJ)
        RESULT = findUsers(TEST_NUMBER, TEST_OFFSET, TEST_LOGIN_SUBSTRING)[0]
        self.assertEquals(RESULT[LOGIN], VALID_RESULT)
        COLLECTION_USERS.insert(TEST_OBJ_1)
        COLLECTION_USERS.insert(TEST_OBJ_2)
        COLLECTION_USERS.insert(TEST_OBJ_3)
        COLLECTION_USERS.insert(TEST_OBJ_4)
        RESULT = findUsers(
            TEST_NUMBER_10,
            TEST_OFFSET,
            TEST_LOGIN_SUBSTRING_TEST)
        self.assertTrue(isSorted(RESULT, LOGIN))
