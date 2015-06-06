#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from bson.objectid import ObjectId
from pymongo import MongoClient
sys.path.append('../')
from  service_not_found_exception import ServiceNotFoundException
from db_model import getServiceIdByName
TEST_ID = ObjectId("55671ae113293c504d515a33")
TEST_DB = 'geomongo'

class test_getServiceIdByName(unittest.TestCase):
    def test_getServiceIdByName_func(self):
        client = MongoClient()
        collection = client[TEST_DB]["services"]
        obj = collection.find_one({"_id": TEST_ID})
        print('Test object: ' + str(obj))
        try:
            testObject =  getServiceIdByName('testservice')
        except ServiceNotFoundException as e:
            self.assertTrue(False)
        with self.assertRaises(ServiceNotFoundException):
            testObject =  getServiceIdByName('OlchikovTestService')