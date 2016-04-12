#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from db_model import addPoints, getDbObject
from bson.objectid import ObjectId

DB = "testservice"
COLLECTION = "points"
ID = "_id"
NAME = 'name'
TEST_POINT1 = {
    'lat': 1.1,
    'lon': 10,
    'alt': 1.1,
    'json': 'd',
    'channel_id': '55671ae113293c504d515a33',
    'bc': False}
TEST_POINT2 = {
    'lat': 1.2,
    'lon': 20,
    'alt': 1.1,
    'json': 'a',
    'channel_id': '55671ae113293c504d515a34',
    'bc': False}


class TestAddPoints(unittest.TestCase):

    def testAddPoints(self):
        db = getDbObject(DB)
        addPoints(DB, [TEST_POINT1, TEST_POINT2])
        obj1 = db[COLLECTION].find_one({
            'channel_id': ObjectId(TEST_POINT1['channel_id'])})
        obj2 = db[COLLECTION].find_one({
            'channel_id': ObjectId(TEST_POINT2['channel_id'])})
        self.assertEqual(obj1['location']['coordinates'][0], 10)
        self.assertEqual(obj2['location']['coordinates'][0], 20)
