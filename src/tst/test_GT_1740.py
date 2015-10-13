#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from pymongo import MongoClient
from db_model import findPoints,getChannelById
import os
import config_reader

TEST_DB = "testservice"
channel_id = '556721a52a2e7febd2744307'
channel_ids = ['556721a52a2e7febd2744307']
channel_name = 'geocoder_plugin_test_channel'
NAME = 'name'
COUNT_RES = 10
JSON = 'json'
ADDRESS = 'address'
NAME_CITY = 'Moscow'

class TestDumpsPluginGeocoder(TestCase):

    def test_Dumps_Plugin_Geocoder_Channels(self):
        res = getChannelById(TEST_DB,channel_id)
        self.assertEqual(res[NAME],channel_name)
        pass

    def test_Dumps_Plugin_Geocoder_Points(self):
        res = findPoints(TEST_DB,channel_ids,1000)
        self.assertEqual(res.count(),COUNT_RES)
        self.assertEqual(res[0][JSON][ADDRESS],NAME_CITY)
