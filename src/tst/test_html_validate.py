#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import html_validate

TEST_FOR_LIST = '123 123'
TEST_LIST = ['123', '123']
TEST_READ_FILE = '[main]\nhost = geomongo\n\
instance_path = instance\nstr = admin/service admin'
NAME_DIR = 'test'
TEST_LIST_1 = ['test/123', 'test/123']


class TestFunctionScriptHtmlValidate(TestCase):

    def testGetListParserParam(self):
        self.assertEqual(
            html_validate.get_list_parser_param(TEST_FOR_LIST), TEST_LIST)

    def testMakeListPathFile(self):
        strp = html_validate.make_list_pathfile(NAME_DIR, TEST_LIST)
        self.assertEqual(TEST_LIST_1, strp)
