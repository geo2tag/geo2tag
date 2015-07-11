#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from bson.objectid import ObjectId
sys.path.append('../')
from db_model import updatePoint, getDbObject
from point_does_not_exist import PointDoesNotExist

DB = "testservice"
COLLECTION = "points"
ID = "_id"
NAME = 'name'
TEST_ID = ObjectId('552833515c0dd1178d37f7cc')
BAD_TEST_ID = ObjectId('111133515c0111178d37f711')
TEST_DICT = {'name': 'test_1319'}
class TestUpdatePoint(unittest.TestCase):
    def testUpdatePoint(self):
        collection = getDbObject(DB)[COLLECTION]
        with self.assertRaises(PointDoesNotExist) as e:
            updatePoint(DB, BAD_TEST_ID, TEST_DICT)
        obj = collection.find_one({ID: TEST_ID})
        updatePoint(DB, TEST_ID, TEST_DICT)
        obj = collection.find_one({ID: TEST_ID})
        self.assertEqual(obj['name'], 'test_1319')
