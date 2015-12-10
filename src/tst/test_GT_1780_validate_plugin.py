#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import os
import shutil
import subprocess

NAME_PLUGIN = 'geocoder'
PY_SCRIPT = 'python ./scripts/validate_plugin.py -name '
RESULT_PEP8 = 'Error code: 0\n'
NAME_FOLDER_TEST = 'test_for_GT_1780'
NAME_FILE = 'test.py'
STR_PEP8_ERROR = "stdout='src/plugins/test_for_GT_1780/test.py:1:80: E501 \
line too long (100 > 79 characters)\n'\nstderr=''\n"
NAME_INIT_FILE = '__init__.py'
NAME_MAIN = 'main.py'
NAME_DEF_GET_PLUGIN_RESOURCE = 'def getPluginResources():\n    pass'
NAME_DEF_GET_PLUGIN_INFO = 'def getPluginInfo():\n    pass'


class TestValidatePlugin(TestCase):

    def testValidatePlugin_DEFAULT(self):
        os.chdir('../..')
        process = subprocess.Popen(
            PY_SCRIPT + NAME_PLUGIN,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
        print process.communicate()
        os.chdir('src/tst')
        print '------'
        self.assertEquals(0, process.poll())

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
        process = subprocess.Popen(
            PY_SCRIPT + NAME_FOLDER_TEST,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
        print process.communicate()
        self.assertEqual(1, process.wait())
        shutil.rmtree('src/plugins/' + NAME_FOLDER_TEST)
        os.chdir("src/tst")
