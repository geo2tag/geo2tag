#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from bson.objectid import ObjectId
from pymongo import MongoClient
sys.path.append('../')
from  service_not_found_exception import ServiceNotFoundException
from db_model import getServiceById
TEST_ID = ObjectId("55671ae113293c504d515a33")
TESTID = "55671ae113293c504d515a33"
TEST_DB = 'geomongo'
BAD_TEST_ID = ObjectId("aa671ae113293c504d515abb")

class test_getServiceById(unittest.TestCase):
    def test_getServiceById_func(self):
        client = MongoClient()
        collection = client[TEST_DB]["services"]
        obj = collection.find_one({"_id": TEST_ID})
        print('Test object: ' + str(obj))
        testObject1 = {}
        try:
            testObject1 =  getServiceById(TEST_ID)
            print('Test object with getServiceById: ' + str(obj))
            print 'testObject1' + str(testObject1)
        except ServiceNotFoundException as e:
            self.assertTrue(False)
        with self.assertRaises(ServiceNotFoundException):
            testObject2 =  getServiceById(BAD_TEST_ID)
            print 'testObject2' + str(testObject2)