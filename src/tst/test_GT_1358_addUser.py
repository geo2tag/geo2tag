from flask import Flask
from pymongo import MongoClient
from unittest import TestCase

import sys
sys.path.append("../")
from config_reader import getDbName
from db_model import getDbObject, getHost, getPort
from user_routines import findUserById, addUser
from user_does_not_exist import UserDoesNotExist

COLLECTION_NAME_USERS = "users"

TEST_ID = 'test_user_id'
TEST_FIRSTNAME = 'test_user_fn'
TEST_LASTNAME = 'test_user_ln'
TEST_EMAIL = 'test_user_email@gmail.com'
TEST_ID_NONE = None

collectionUsers = getDbObject(getDbName())[COLLECTION_NAME_USERS]

app = Flask(__name__)


class TestaddUserById(TestCase):

    def testaddUserById(self):
        collectionUsers.drop()
        result_id = addUser(TEST_ID, TEST_FIRSTNAME, TEST_LASTNAME, TEST_EMAIL)
        print result_id
        self.assertEqual(TEST_ID, result_id)
        result_id = addUser(TEST_ID, TEST_FIRSTNAME, TEST_LASTNAME, TEST_EMAIL)
        print result_id
        self.assertEqual(TEST_ID, result_id)
