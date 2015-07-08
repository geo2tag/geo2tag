#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')
from db_model import deleteChannelById, getChannelsList, getDbObject
from config_reader import getHost, getPort
from channel_does_not_exist import ChannelDoesNotExist

SERVICE_NAME = 'testservice'
db = getDbObject(SERVICE_NAME)
CHANNELS = 'channels'
class TestDeleteChannelById(unittest.TestCase):
    def testDeleteChannelById(self):
        result = db[CHANNELS].insert({'name': 'test_GT-1289'})
        BAD_ID = db[CHANNELS].insert({'name': 'test_GT-1289_2'})
        result = db[CHANNELS].remove({'name': 'test_GT-1289_2'})
        obj = db[CHANNELS].find({'name': 'test_GT-1289'})
        obj = list(obj)
        obj_string = obj[0].get('_id')
        deleteChannelById(SERVICE_NAME, obj_string)
        with self.assertRaises(ChannelDoesNotExist) as e:
            deleteChannelById(SERVICE_NAME, BAD_ID) 
