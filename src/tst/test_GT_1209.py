#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from bson.objectid import ObjectId
from service_not_exist_exception import ServiceNotExistException
from db_model import getServiceById, getDbObject
TEST_ID = ObjectId("55671ae113293c504d515a33")
TESTID = "55671ae113293c504d515a33"
TEST_DB = 'geomongo'
BAD_TEST_ID = ObjectId("aa671ae113293c504d515abb")


class test_getServiceById(unittest.TestCase):

    def test_getServiceById_func(self):
        collection = getDbObject(TEST_DB)["services"]
        obj = collection.find_one({"_id": TEST_ID})
        print('Test object: ' + unicode(obj))
        testObject1 = {}
        try:
            testObject1 = getServiceById(TEST_ID)
            print('Test object with getServiceById: ' + unicode(obj))
            print 'testObject1' + unicode(testObject1)
        except ServiceNotExistException:
            self.assertTrue(False)
        with self.assertRaises(ServiceNotExistException):
            testObject2 = getServiceById(BAD_TEST_ID)
            print 'testObject2' + unicode(testObject2)
