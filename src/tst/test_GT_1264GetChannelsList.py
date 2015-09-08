#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from bson.objectid import ObjectId
sys.path.append('../')
from db_model import getChannelsList

TEST_SERVICE = 'testservice'
TEST_LIST = [{u'json': {},
              u'_id': ObjectId('556721a52a2e7febd2744202'),
              u'name': u'test_channel_2',
              u'owner_id': u'STUB'},
             {u'json': {},
              u'_id': ObjectId('556721a52a2e7febd2744204'),
              u'name': u'test_channel_4',
              u'owner_id': u'STUB'},
             {u'json': {},
              u'_id': ObjectId('556721a52a2e7febd2744205'),
              u'name': u'test_channel_5',
              u'owner_id': u'STUB'}]
TEST_LIST2 = [{u'json': {},
               u'_id': ObjectId('556721a52a2e7febd2744202'),
               u'name': u'test_channel_2',
               u'owner_id': u'STUB'}]


class TestGetChannelsList(unittest.TestCase):

    def testGetChannelsList(self):
        result = getChannelsList(TEST_SERVICE, 'test_channel_', 3, 1)
        self.assertEquals(list(result), TEST_LIST)
        result = getChannelsList(TEST_SERVICE, 'test_channel_GT_1264', 3, 1)
        self.assertEquals(list(result), [])
        result = getChannelsList(TEST_SERVICE, 'test_channel_2', None, None)
        self.assertEquals(list(result), TEST_LIST2)
