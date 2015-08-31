#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from pymongo import MongoClient
sys.path.append('../')
from bson.objectid import ObjectId
from point_list_resource_parser import validatePointsList

TEST_ARGS = [{'lat': 1.1, 'lon': 1.1, 'alt': 5, 'json': {}, 'channel_id': ''}]
INCORRECT_ARGS1 = [{'lat': 1}]
INCORRECT_ARGS2 = [{'lat': 1.1, 'lon': 1.1,
                    'alt': 'f', 'json': {}, 'channel_id': ''}]


class TestValidatePointsList(unittest.TestCase):

    def testValidatePointsList(self):
        args = validatePointsList(TEST_ARGS)
        self.assertEqual(args, TEST_ARGS)
        with self.assertRaises(ValueError) as e:
            args = validatePointsList(INCORRECT_ARGS1)
        with self.assertRaises(ValueError) as e:
            args = validatePointsList(INCORRECT_ARGS2)
