#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
from datetime import datetime
sys.path.append('../plugins/ok_import/')
from open_karelia_object_to_point_translator import OpenKareliaObjectToPointTranslator


class Test_GT_1510_translate_date(TestCase):

    def test_GT_1510_translate_date(self):
        obj = OpenKareliaObjectToPointTranslator(
            'image_url', 'object_url', {
                'year': '1249', 'century': 15, 'millenium': 2},
                                                 'test_version', 'test_import', 'channelId')
        self.assertEquals(type(obj.translateDate()), type(datetime.now()))
        obj = OpenKareliaObjectToPointTranslator(
            'image_url', 'object_url', {'century': 21, 'millenium': '2'},
                                                'test_version', 'test_import', 'channelId')
        self.assertEquals(type(obj.translateDate()), type(datetime.now()))
        obj = OpenKareliaObjectToPointTranslator(
            'image_url', 'object_url', {'year': '1249'},
                                                'test_version', 'test_import', 'channelId')
        self.assertEquals(type(obj.translateDate()), type(datetime.now()))
