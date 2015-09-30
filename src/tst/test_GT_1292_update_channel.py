#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from db_model import updateChannel, getDbObject
from channel_does_not_exist import ChannelDoesNotExist

DB = "testservice"
COLLECTION = "channels"
ID = "_id"
NAME = 'name'


class TestUpdateChannel(unittest.TestCase):

    def testUpdateChannel(self):
        collection = getDbObject(DB)[COLLECTION]
        obj_id = collection.save({NAME: 'test_GT_1292'})
        with self.assertRaises(ChannelDoesNotExist) as e:
            updateChannel('testservice', '111', 'test', None, None)
        updateChannel('testservice', obj_id, 'test', 1, 2)
        obj = collection.find_one({ID: obj_id})
        self.assertEqual(obj['name'], 'test')
        self.assertEqual(obj['json'], 1)
        self.assertEqual(obj['acl'], 2)
