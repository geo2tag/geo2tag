#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from bson.objectid import ObjectId
from metadata_does_not_exist_exception import MetadataDoesNotExistException
from db_model import getMetadataById, getDbObject

TEST_ID = ObjectId("55671ae113293c504d515a33")
TEST_DB = 'testservice'
BAD_TEST_ID = ObjectId("aa671ae113293c504d515abb")
TEST_COLLECTION = 'metadata'
TEST_DATA = {'_id': TEST_ID, 'a': '1', 'b': '2'}


class testGetMetadataById(unittest.TestCase):

    def testGetMetadataById(self):
        collection = getDbObject(TEST_DB)[TEST_COLLECTION]
        collection.insert(TEST_DATA)
        obj = collection.find_one({"_id": TEST_ID})
        try:
            result = getMetadataById(TEST_DB, TEST_ID)
            self.assertEqual(obj, result)
        except MetadataDoesNotExistException:
            self.assertTrue(False)
        with self.assertRaises(MetadataDoesNotExistException):
            result = getMetadataById(TEST_DB, BAD_TEST_ID)
