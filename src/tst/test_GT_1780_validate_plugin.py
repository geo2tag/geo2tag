#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import os
import shutil

NAME_PLUGIN = 'geocoder'
PY_SCRIPT = 'python ./scripts/validate_plugin.py '
RESULT_PEP8 = 'Error code: 0\n'
NAME_FOLDER_TEST = 'test_for_GT_1780'
NAME_FILE = 'test.py'
NAME_INIT_FILE = '__init__.py'
NAME_MAIN = 'main.py'
NAME_DEF_GET_PLUGIN_RESOURCE = 'def getPluginResources():\n    pass'
NAME_DEF_GET_PLUGIN_INFO = 'def getPluginInfo():\n    pass'
STR_PEP8_ERROR = 'src/plugins/test_for_GT_1780/test.py:1:80: \
E501 line too long (100 > 79 characters)\n\nError code: 1\n'


class TestValidatePlugin(TestCase):

    def testValidatePlugin_DEFAULT(self):
        os.chdir('../..')
        data = os.popen(PY_SCRIPT + NAME_PLUGIN).read()
        self.assertEqual(RESULT_PEP8, data)
        os.chdir('src/tst')

    def testValidatePlugin_MakePlugin(self):
        os.chdir('../plugins/')
        os.mkdir(NAME_FOLDER_TEST)
        os.chdir(NAME_FOLDER_TEST)
        file_init = open(NAME_INIT_FILE, 'w+')
        file_init.close()
        file_main = open(NAME_MAIN, 'w+')
        file_main.write(NAME_DEF_GET_PLUGIN_RESOURCE)
        file_main.write('\n\n\n' + NAME_DEF_GET_PLUGIN_INFO + '\n')
        file_main.close()
        file_test = open(NAME_FILE, 'w+')
        i = 0
        while i < 100:
            file_test.write('s')
            i = i + 1
        file_test.write('\n')
        file_test.close()
        os.chdir('../../..')
        data = os.popen(PY_SCRIPT + NAME_FOLDER_TEST).read()
        self.assertEqual(data, STR_PEP8_ERROR)
        shutil.rmtree('src/plugins/' + NAME_FOLDER_TEST)
        os.chdir('src/tst')
