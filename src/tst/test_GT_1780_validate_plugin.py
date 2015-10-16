#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import os
import sys

NAME_PLUGIN = 'geocoder'
PY_SCRIPT = 'python ./scripts/validate_plugin.py ' + NAME_PLUGIN
RESULT_PEP8 = 'Error code: 0\n'


class TestValidatePlugin(TestCase):

    def testValidatePlugin_DEFAULT(self):
        os.chdir('../..')
        data = os.popen(PY_SCRIPT).read()
        self.assertEqual(RESULT_PEP8, data)
        os.chdir('src/tst')
