#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from bson.objectid import ObjectId
from db_model import addChannel, getDbObject
from config_reader import getHost, getPort

TEST_SERVICE = 'testservice'
NAME = 'test_name'
JSON = 'test_json'
OWNER_ID = 'test_owner_id'
OWNER_GROUP = 'STUB'
SERVICE_NAME = 'testservice'
ACl = 777

db = getDbObject(SERVICE_NAME)


class TestAddChannel(unittest.TestCase):

    def testAddChannel(self):
        result = addChannel(NAME, JSON, OWNER_ID, SERVICE_NAME)
        self.assertNotEqual(result, None)
        self.assertNotEquals(list(db['channels'].find({'_id': result})), [])
        db['channels'].remove({'_id': result})
