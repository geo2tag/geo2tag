#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from pymongo import MongoClient
sys.path.append('../')
from db_model import getChannelById
from channel_does_not_exist import ChannelDoesNotExist
from bson.objectid import ObjectId

DB = "testservice"
COLLECTION = "channels"
ID = "_id"
NAME = 'name'

class TestGetChannelById(unittest.TestCase):
    def testGetChannelById(self):
        client = MongoClient()
        collection = client[DB][COLLECTION]
        obj_id = collection.save({NAME: 'test_GT_1286'})
        with self.assertRaises(ChannelDoesNotExist) as e:
            getChannelById('testservice', '111')
        obj = getChannelById('testservice', obj_id)
        self.assertEqual(obj['name'], 'test_GT_1286')