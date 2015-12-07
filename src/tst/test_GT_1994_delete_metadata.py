#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from bson.objectid import ObjectId
from db_model import deleteMetadataById, getDbObject

TEST_ID = ObjectId("55671111132931504d515222")
TEST_DB = "testservice"
TEST_COLLECTION = "metadata"
ID = "_id"
TEST_DATA = {'_id': TEST_ID, 'a': '1', 'b': '2'}


class TestDeleteMetadataById(unittest.TestCase):

    def testDeleteMetadataById(self):
        collection = getDbObject(TEST_DB)[TEST_COLLECTION]
        collection.insert(TEST_DATA)
        deleteMetadataById(TEST_DB, TEST_ID)
        obj = collection.find_one({ID: TEST_ID})
        self.assertEqual(obj, None)
