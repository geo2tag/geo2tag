#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from db_model import getChannelByName, getDbObject
from channel_does_not_exist import ChannelDoesNotExist

DB = "testservice"
COLLECTION = "channels"
ID = "_id"
NAME = 'name'


class TestGetChannelByName(unittest.TestCase):

    def testGetChannelByName(self):
        db = getDbObject(DB)
        obj_id = db[COLLECTION].save({NAME: 'test_GT_1288'})
        with self.assertRaises(ChannelDoesNotExist):
            getChannelByName('testservice', '111')
        obj = getChannelByName('testservice', 'test_GT_1288')
        self.assertEqual(obj['_id'], obj_id)
