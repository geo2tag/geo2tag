from flask import Flask
from unittest import TestCase
from config_reader import getDbName
from db_model import getDbObject
from user_routines import addUser

COLLECTION_NAME_USERS = "users"

TEST_ID = 'test_user_id'
TEST_FIRSTNAME = 'test_user_fn'
TEST_LASTNAME = 'test_user_ln'
TEST_EMAIL = 'test_user_email@gmail.com'
TEST_LOGIN = 'test_user_email'
TEST_ID_NONE = None

collectionUsers = getDbObject(getDbName())[COLLECTION_NAME_USERS]

app = Flask(__name__)


class TestaddUserById(TestCase):

    def testaddUserById(self):
        collectionUsers.drop()
        result_id = addUser(
            TEST_ID,
            TEST_FIRSTNAME,
            TEST_LASTNAME,
            TEST_EMAIL,
            TEST_LOGIN)
        self.assertEqual(TEST_ID, result_id)
        result_id = addUser(
            TEST_ID,
            TEST_FIRSTNAME,
            TEST_LASTNAME,
            TEST_EMAIL,
            TEST_LOGIN)
        self.assertEqual(TEST_ID, result_id)
