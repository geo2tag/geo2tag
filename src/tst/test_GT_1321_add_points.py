#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from db_model import addPoints, getDbObject

DB = "testservice"
COLLECTION = "points"
ID = "_id"
NAME = 'name'
TEST_POINT1 = {
    'lat': 1.1,
    'lon': 10,
    'alt': 1.1,
    'json': 'd',
    'channel_id': '3',
    'bc': False}
TEST_POINT2 = {
    'lat': 1.2,
    'lon': 20,
    'alt': 1.1,
    'json': 'a',
    'channel_id': '5',
    'bc': False}


class TestAddPoints(unittest.TestCase):

    def testAddPoints(self):
        db = getDbObject(DB)
        addPoints(DB, [TEST_POINT1, TEST_POINT2])
        obj1 = db[COLLECTION].find_one({'channel_id': '3'})
        obj2 = db[COLLECTION].find_one({'channel_id': '5'})
        self.assertEqual(obj1['location']['coordinates'][0], 10)
        self.assertEqual(obj2['location']['coordinates'][0], 20)
