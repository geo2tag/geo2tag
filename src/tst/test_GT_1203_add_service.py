#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from pymongo import MongoClient
sys.path.append('../')
from db_model import addService

class TestAddService(unittest.TestCase):
    def testAddService(self):
        client = MongoClient()
        collection = client["geomongo"]["services"]
        obj = addService("testservice", 1, ' ')
        self.assertEqual(obj, False)
        obj_id = addService("test_GT_1203", 1, ' ')
        obj = collection.find_one({'_id' : obj_id})
        self.assertNotEqual(obj, None)
