from flask import Flask
from pymongo import MongoClient
from unittest import TestCase

import sys
sys.path.append("../")
from config_reader import getDbName
from db_model import getDbObject, getHost, getPort
from user_routines import findUserById
from user_does_not_exist import UserDoesNotExist

COLLECTION_NAME_USERS = "users"

FIELD_USER_ID = "user_id"

GOOD_USER_ID = "user_id_5"
BAD_USER_ID = "user_id"

collectionUsers = getDbObject(getDbName())[COLLECTION_NAME_USERS]

app = Flask(__name__)

class TestFindUserById(TestCase):
    def setUp(self):
        for i in range(10) :
            collectionUsers.insert(
                {
                    FIELD_USER_ID : FIELD_USER_ID + "_" + str(i),
                    "first_name":"string",
                    "last_name":"string"
                }
            )
    def tearDown(self):
        collectionUsers.drop()
    def testFindUserById(self):
        with self.assertRaises(UserDoesNotExist) as e:
            findUserById(BAD_USER_ID)
        self.assertTrue(findUserById(GOOD_USER_ID)[FIELD_USER_ID] == GOOD_USER_ID)
