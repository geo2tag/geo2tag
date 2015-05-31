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
        print type(TEST_ID)
        print('Test object: ' + str(obj))
        try:
            testObject =  getServiceIdByName('testservice')
        except Exception, e:
            ServiceException = ServiceNotFoundException(e)
            self.assertTrue(testObject.get('_id') == obj.get('_id'))
        try:
            testObject =  getServiceIdByName('OlchikovTestService')
        except Exception, e:
            ServiceException = ServiceNotFoundException(e)
            self.assertTrue(('Service not found', 400) == ServiceException.getReturnObject())