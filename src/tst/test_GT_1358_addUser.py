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
        user = collectionUsers.find_one({'_id': result_id})
        self.assertEqual(TEST_ID, user.get('_id'))
        self.assertEqual(TEST_LOGIN, user.get('login'))
        self.assertEqual(TEST_EMAIL, user.get('email'))
        self.assertEqual(TEST_LASTNAME, user.get('last_name'))
        self.assertEqual(TEST_FIRSTNAME, user.get('first_name'))