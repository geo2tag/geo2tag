#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from bson.objectid import ObjectId
sys.path.append('../')
from service_not_exist_exception import ServiceNotExistException
from db_model import getServiceIdByName, getDbObject
TEST_ID = ObjectId("55671ae113293c504d515a33")
TEST_DB = 'geomongo'


class test_getServiceIdByName(unittest.TestCase):

    def test_getServiceIdByName_func(self):
        collection = getDbObject(TEST_DB)["services"]
        obj = collection.find_one({"_id": TEST_ID})
        print('Test object: ' + str(obj))
        try:
            testObject = getServiceIdByName('testservice')
        except ServiceNotExistException as e:
            self.assertTrue(False)
        with self.assertRaises(ServiceNotExistException):
            testObject = getServiceIdByName('OlchikovTestService')
