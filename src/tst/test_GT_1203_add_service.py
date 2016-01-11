#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from db_model import addService, getDbObject
from service_already_exists_exception import ServiceAlreadyExistsException
from test_GT_1329_addServiceDb import checkGeneratedDb

DB = "geomongo"
COLLECTION = "services"
ID = "_id"
INVALID_SERVICE_NAME = "testservice"
VALID_SERVICE_NAME = "test_GT_1203"


class TestAddService(unittest.TestCase):

    def testAddService(self):
        collection = getDbObject(DB)[COLLECTION]
        with self.assertRaises(ServiceAlreadyExistsException):
            obj = addService(INVALID_SERVICE_NAME, 1, ' ')
        obj_id = addService(VALID_SERVICE_NAME, 1, ' ')
        obj = collection.find_one({ID: obj_id})
        self.assertNotEqual(obj, None)

        checkGeneratedDb(self, VALID_SERVICE_NAME)
