#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import os
import sys

NAME_PLUGIN = 'test_for_validate_plugin'
PY_SCRIPT = 'python ./scripts/validate_plugin.py ' + NAME_PLUGIN
RESULT_PEP8 = 'src/plugins/test_for_validate_plugin/main.py:11:80: E501 line too long (145 > 79 characters)\n\nError code: 1\n'
FORMAT = '"%\(code\)s"'
RESULT_PEP8_FORMAT = 'E501\n\nError code: 1\n'


class TestValidatePlugin(TestCase):

    def testValidatePlugin_DEFAULT(self):
        os.chdir('../..')
        data = os.popen(PY_SCRIPT).read()
        self.assertEqual(RESULT_PEP8, data)
        os.chdir('src/tst')

    def testValidatePlugin_Myformat(self):

        os.chdir('../..')
        data = os.popen(PY_SCRIPT + ' ' + FORMAT).read()
        self.assertEqual(RESULT_PEP8_FORMAT, data)
        os.chdir('src/tst')
