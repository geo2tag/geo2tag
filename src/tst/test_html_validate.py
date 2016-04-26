#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import html_validate
import os
import subprocess

TEST_FOR_LIST = '123 123'
TEST_LIST = ['123', '123']
str_OK = 'http://geomongo/instance/status'
RES_OK = 'OK'
TEXT_STR1 = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">\
<html>\
  <head>\
    <title>\
      Test document\
    </title>\
  </head>\
  <body>\
    <p>\
      para which has enough text to cause a line break, \
      and so test the wrapping mechanism for long lines.\
    </p>\
    <pre>\
        This is\
        <em>genuine\
        preformatted</em>\
        text\
    </pre>\
    <ul>\
      <li>1st list item\
      </li>\
      <li>2nd list item\
      </li>\
    </ul><!-- end comment -->\
  </body>\
</html>'
TEXT_STR2 = '<html>\
  <head>\
  </head>\
  <body>\
    <p>para which has enough text to cause a line break,\
    and so test the wrapping mechanism for long lines.</p>\
<pre>\
This is\
<em>genuine\
       preformatted</em>\
   text\
</pre>\
    <ul>\
      <li>1st list item</li>\
      <li>2nd list item</li>\
    <!-- end comment -->\
  </body>\
</html>'
FILE_NAME = 'testfile.py'
PY_SCRIPT = "python scripts/html_validate.py --conf \
scripts/validhtml.ini --url 'status'"
PATH = '../..'
PATH_HOME = 'src/tst'


class TestFunctionScriptHtmlValidate(TestCase):

    def testGetListParserParam(self):
        self.assertEqual(
            html_validate.get_list_parser_param(TEST_FOR_LIST), TEST_LIST)

    def testRequest(self):
        res = html_validate.url_request(str_OK)
        self.assertEqual(res.read(), RES_OK)

    def testValidate1(self):
        res = html_validate.validate_tidy(TEXT_STR1, FILE_NAME)
        self.assertEqual(res, 0)

    def testValidate2(self):
        res = html_validate.validate_tidy(TEXT_STR2, FILE_NAME)
        self.assertEqual(res, 1)

    def testScriptRun(self):
        os.chdir(PATH)
        process = subprocess.Popen(
            PY_SCRIPT,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
        process.communicate()
        os.chdir(PATH_HOME)
        self.assertEquals(1, process.poll())
