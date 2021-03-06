#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from db_model import getChannelById, getDbObject
from channel_does_not_exist import ChannelDoesNotExist

DB = "testservice"
COLLECTION = "channels"
ID = "_id"
NAME = 'name'


class TestGetChannelById(unittest.TestCase):

    def testGetChannelById(self):
        db = getDbObject(DB)
        obj_id = db[COLLECTION].save({NAME: 'test_GT_1286'})
        with self.assertRaises(ChannelDoesNotExist):
            getChannelById('testservice', '111111111111111111111111')
        obj = getChannelById('testservice', obj_id)
        self.assertEqual(obj['name'], 'test_GT_1286')
