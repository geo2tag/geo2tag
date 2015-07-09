import pymongo
import unittest
from flask import session
from os import urandom
from flask import Flask, request, session

from db_model import getDbObject
from log import writeInstanceLog

import sys
sys.path.append('../')
from config_reader import getDbName, getInstancePrefix


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
    def testUserRoutins(self) :
        with app.test_client() as c:
            with c.session_transaction() as sess:
                #Emulating login session
                with app.test_request_context(LOGOIN_REQUEST_CONTEXT + REQUEST_PARAM) :
                    #from user_routines - logUserIn
                    #-----------------------------------------------
                    sess[USER_ID_FIELD] = TEST_ID
                    writeInstanceLog(sess[USER_ID_FIELD], 'login')
                    print "ALL"
                    for i in list(COLLECTION_LOG.find()) :
                        print i
                    print "ALL"
                    #-----------------------------------------------
                    self.assertTrue(sess[USER_ID_FIELD] == TEST_ID)
                    #Testing writing in log
                    IS_USER_LOGIN = COLLECTION_LOG.find({USER_ID_FIELD : TEST_ID, MESSAGE : MSG_LOGIN}, None, 0, 1).sort("_id", pymongo.DESCENDING)
                    self.assertTrue(IS_USER_LOGIN.count() == 1)
                    self.assertTrue(list(IS_USER_LOGIN)[0][MESSAGE] == MSG_LOGIN)
                    print "LAST"
                    for i in COLLECTION_LOG.find({USER_ID_FIELD : TEST_ID, MESSAGE : MSG_LOGIN}, None, 0, 1).sort("_id", pymongo.DESCENDING) :
                        print i
                    print "LAST"
                    print "CURRENT AFTER LOGIN SESSION"
                    print sess
                    #Emulating logout session
                    with app.test_request_context(LOGOUT_REQUEST_CONTEXT + REQUEST_PARAM) :
                        #checking if session is still alive
                        print "CURRENT AFTER LOGIN SESSION IN LOGOUT REQUEST"
                        print sess
                        self.assertTrue(sess[USER_ID_FIELD] == TEST_ID)
                        #from user_routines - logUserOut
                        #-----------------------------------------------
                        SESSION_VALUE = "Wasn't logged in"
                        if USER_ID_FIELD in sess :
                            SESSION_VALUE = sess.pop(USER_ID_FIELD)
                        writeInstanceLog(SESSION_VALUE, 'logout')
                        self.assertTrue(USER_ID_FIELD not in sess)
                        print "CURRENT AFTER LOGOUT SESSION"
                        print sess
                        print "ALL"
                        for i in list(COLLECTION_LOG.find()) :
                            print i
                        print "ALL"
                        #-----------------------------------------------
                        #Testing writing in log
                        IS_USER_LOGOUT = COLLECTION_LOG.find({USER_ID_FIELD : TEST_ID, MESSAGE : MSG_LOGOUT}, None, 0, 1).sort("_id", pymongo.DESCENDING)
                        self.assertTrue(IS_USER_LOGOUT.count() == 1)
                        self.assertTrue(list(IS_USER_LOGOUT)[0][MESSAGE] == MSG_LOGOUT)
                        print "LAST"
                        for i in COLLECTION_LOG.find({USER_ID_FIELD : TEST_ID, MESSAGE : MSG_LOGOUT}, None, 0, 1).sort("_id", pymongo.DESCENDING) :
                            print i
                        print "LAST"