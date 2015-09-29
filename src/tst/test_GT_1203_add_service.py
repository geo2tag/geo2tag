#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from db_model import addService, getDbObject
from service_already_exists_exception import ServiceAlreadyExistsException

DB = "geomongo"
COLLECTION = "services"
ID = "_id"


class TestAddService(unittest.TestCase):

    def testAddService(self):
        collection = getDbObject(DB)[COLLECTION]
        with self.assertRaises(ServiceAlreadyExistsException) as e:
            obj = addService("testservice", 1, ' ')
        obj_id = addService("test_GT_1203", 1, ' ')
        obj = collection.find_one({ID: obj_id})
        self.assertNotEqual(obj, None)
