#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
sys.path.append('../plugins/ok_import/')
sys.path.append('../open_data_import')
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator
from datetime import datetime

TEST_OBJ = {
    'json': {
        'import_source': 'test_import',
        'version': 'test_version',
        'image_url': u'image_url',
        'name': 'test_GT_1499',
        'source_url': u'image_url111'},
    'channelId': 'channelId',
    'location': {
        'type': 'Point',
        'coordinates': [
                1,
                2]},
    'alt': 0}


class TestOKPointTranslator(TestCase):
    def setUp(self):
        obj = OpenKareliaObjectToPointTranslator(
            {'image_url': 'image_url', 'source_url': 'image_url111'},
            {
                'name': ['test_GT_1499'],
                '_id': '111',
                'latitude': 1,
                'longitude': 2},
            'test_version',
            'test_import',
            'channelId')
        self.test_obj = obj.getPoint()
    def testOKPointTranslator(self):
        self.assertEquals(TEST_OBJ['json'], self.test_obj['json'])
        self.assertEquals(TEST_OBJ['location'], self.test_obj['location'])
    def testOkPointTranslatorBC(self):
        self.assertEqual(self.test_obj['bc'], False)
