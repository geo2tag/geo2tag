#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from pymongo import MongoClient
from db_model import getAllChannelIds
import config_reader

SERVICE_NAME = 'testservice'
TEST_ID = u'5704f32902c1c90072955867'
db = MongoClient(config_reader.getHost(),
                 config_reader.getPort())[SERVICE_NAME]
CHANNELS_COLLECTION = 'channels'


class TestgetAllChannelIds(TestCase):

    def testgetAllChannelIds_id(self):
        result = getAllChannelIds(SERVICE_NAME)
        self.assertEqual(result[0], TEST_ID)

    def testgetAllChannelIds_count(self):
        count_channels = db[CHANNELS_COLLECTION].count()
        result = getAllChannelIds(SERVICE_NAME)
        self.assertEqual(len(result), count_channels)
