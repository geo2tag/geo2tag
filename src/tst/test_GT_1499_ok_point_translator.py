#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
sys.path.append('../plugins/ok_import/')
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator

TEST_OBJ = {'name': 'test_GT_1499', 'channelId': ['channelId1', 'channelId2'], 'source_url': 'object_url', 
            'version': 'test_version', 'import_source': 'test_import', 'image_url': 'image_url'}

class TestOKPointTranslator(TestCase):
    def testOKPointTranslator(self):
        obj = OpenKareliaObjectToPointTranslator('image_url', 'object_url', {'name': 'test_GT_1499'}, 'test_version', 
        	                                     'test_import', ['channelId1', 'channelId2'])
        test_obj = obj.getPoint()
        self.assertEquals(TEST_OBJ, test_obj)