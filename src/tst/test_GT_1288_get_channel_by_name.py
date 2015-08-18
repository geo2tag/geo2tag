#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')
from db_model import getChannelByName, getDbObject
from channel_does_not_exist import ChannelDoesNotExist
from bson.objectid import ObjectId

DB = "testservice"
COLLECTION = "channels"
ID = "_id"
NAME = 'name'


class TestGetChannelByName(unittest.TestCase):

    def testGetChannelByName(self):
        db = getDbObject(DB)
        obj_id = db[COLLECTION].save({NAME: 'test_GT_1288'})
        with self.assertRaises(ChannelDoesNotExist) as e:
            getChannelByName('testservice', '111')
        obj = getChannelByName('testservice', 'test_GT_1288')
        self.assertEqual(obj['_id'], obj_id)
