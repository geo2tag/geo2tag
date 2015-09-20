#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import sys
sys.path.append('../plugins/ok_import/')

from open_karelia_objects_parser import OpenKareliaObjectsParser

TEST_JSON = '[{"name": "test1", "test": "test"}, {"name": "test2"}]'
TEST_OBJ1 = {"name": "test1", "test": "test"}
TEST_OBJ2 = {"name": "test2"}


class TestOKObjectsParser(TestCase):

    def testOKObjectsParser(self):
        obj = OpenKareliaObjectsParser(TEST_JSON)
        test_obj = obj.parse()
        self.assertEquals(TEST_OBJ1, test_obj[0])
        self.assertEquals(TEST_OBJ2, test_obj[1])
