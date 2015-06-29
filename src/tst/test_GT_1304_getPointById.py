#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from pymongo import MongoClient
sys.path.append('../')
from db_model import getPointById, getDbObject
from point_does_not_exist import PointDoesNotExist
from bson.objectid import ObjectId

DB = "testservice"
COLLECTION = "points"
ID = "_id"
NAME = 'name'

class TestGetPointById(unittest.TestCase):
    def testGetPointById(self):
        db = getDbObject(DB)
        obj_id = db[COLLECTION].save({NAME: 'test_GT_1304'})
        with self.assertRaises(PointDoesNotExist) as e:
            getPointById('testservice', '111111111111111111111111')
        obj = getPointById('testservice', obj_id)
        self.assertEqual(obj['name'], 'test_GT_1304')