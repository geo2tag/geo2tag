#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from bson.objectid import ObjectId
from db_model import setMetadata, getDbObject

TEST_ID = ObjectId("55671ae113293c504d515a33")
TEST_DB = 'testservice'
TEST_COLLECTION = 'metadata'
TEST_DATA = {'_id': TEST_ID, 'a': '1', 'b': '2'}
JSON = 'json'
ID = '_id'


class TestSetMetadata(unittest.TestCase):

    def testSetMetadata(self):
        collection = getDbObject(TEST_DB)[TEST_COLLECTION]
        setMetadata(TEST_DB, TEST_DATA, TEST_ID)
        obj = collection.find_one({ID: TEST_ID})
        self.assertEqual(obj[JSON], TEST_DATA)
