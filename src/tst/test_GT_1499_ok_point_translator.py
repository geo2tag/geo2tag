#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
sys.path.append('../plugins/ok_import/')
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator
from datetime import datetime

TEST_OBJ = {
    'json': {
        'import_source': 'test_import',
        'version': 'test_version',
        'image_url': 'image_url',
        'name': 'test_GT_1499',
        'source_url': 'object_url111'},
    'channelId': 'channelId',
    'location': {
        'type': 'Point',
        'coordinates': [
                1,
                2]},
    'alt': 0}


class TestOKPointTranslator(TestCase):

    def testOKPointTranslator(self):
        obj = OpenKareliaObjectToPointTranslator(
            'image_url',
            'object_url',
            {
                'name': ['test_GT_1499'],
                '_id': '111',
                'latitude': 1,
                'longitude': 2},
            'test_version',
            'test_import',
            'channelId')
        test_obj = obj.getPoint()
        self.assertEquals(TEST_OBJ['json'], test_obj['json'])
        self.assertEquals(TEST_OBJ['location'], test_obj['location'])
        self.assertEqual(test_obj['bc'], False)
