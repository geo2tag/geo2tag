#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
sys.path.append('../')
from config_reader import getHost, getPort, getDbName
from db_model import removeService, getServiceIdByName, getDbObject
from service_not_exist_exception import ServiceNotExistException

db = getDbObject() 
COLLECTION = 'services'
NAME = 'name'
TEST_OBJECT = 'test_GT_1208'

class TestRemoveService(TestCase):
    def testRemoveService(self):
        db[COLLECTION].save({NAME : TEST_OBJECT})
        removeService(TEST_OBJECT)
        with self.assertRaises(ServiceNotExistException) as e:
            getServiceIdByName(TEST_OBJECT)
