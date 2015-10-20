#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from open_data_object_to_point_translator import OpenDataToPointTranslator

TEST_OBJ = {
    'json': {'version': 'test_version',
             'import_source': 'test_import'},
}


class TestOKPointTranslator(TestCase):

    def setUp(self):
        obj = OpenDataToPointTranslator(
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
