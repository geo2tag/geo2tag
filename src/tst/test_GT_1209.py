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

class test_getServiceById(unittest.TestCase):
    def test_getServiceById_func(self):
        client = MongoClient()
        collection = client[TEST_DB]["services"]
        obj = collection.find_one({"_id": TEST_ID})
        print('Test object: ' + str(obj))
        try:
            testObject1 =  getServiceById(TEST_ID)
            print('Test object with getServiceById: ' + str(obj))
        except Exception, e:
            ServiceException = ServiceNotFoundException(e)
            self.assertTrue(testObject1.get('_id') == obj.get('_id'))
        try:
            testObject2 =  getServiceById('aa671ae113293c504d515abb')
        except Exception, e:
            ServiceException = ServiceNotFoundException(e)
            self.assertTrue(('Service not found', 400) == ServiceException.getReturnObject())