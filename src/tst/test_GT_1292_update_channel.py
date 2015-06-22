#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from pymongo import MongoClient
sys.path.append('../')
from db_model import updateChannel
from channel_does_not_exist import ChannelDoesNotExist

DB = "testservice"
COLLECTION = "channels"
ID = "_id"
NAME = 'name'

class TestUpdateChannel(unittest.TestCase):
    def testUpdateChannel(self):
        client = MongoClient()
        collection = client[DB][COLLECTION]
        obj_id = collection.save({NAME: 'test_GT_1292'})
        with self.assertRaises(ChannelDoesNotExist) as e:
            updateChannel('testservice', '111', 'test', None, None)
        updateChannel('testservice', obj_id, 'test', 1, 2)
        obj = collection.find_one({ID: obj_id})
        self.assertEqual(obj['name'], 'test')
        self.assertEqual(obj['json'], 1)
        self.assertEqual(obj['acl'], 2)