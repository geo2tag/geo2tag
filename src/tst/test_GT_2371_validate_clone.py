#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import os
import shutil
import subprocess

PY_SCRIPT = 'python scripts/validate_clone.py --file '
NAME_FILE = 'test_forclonedigger.py'
TEXT_PROG_NO_CLONE = 'def fibonacci(max):\n    a = 1\n    b = 1\n    print(a+b)'
PATH_MAIN_FILE = 'src/main.py'
PATH_TEST_FILE = 'src/tst/' + NAME_FILE


class TestValidateClone(TestCase):

    def testValidateClone_Clone(self):
        os.chdir('../..')
        process = subprocess.Popen(
            PY_SCRIPT + PATH_MAIN_FILE,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
        process.communicate()
        os.chdir('src/tst')
        self.assertEquals(1, process.poll())

    def testValidatePlugin_MakeFileNoClone(self):
        file_main = open(NAME_FILE, 'w+')
        file_main.write(TEXT_PROG_NO_CLONE)
        file_main.close()
        os.chdir('../..')
        process = subprocess.Popen(
            PY_SCRIPT + PATH_TEST_FILE,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
        process.communicate()
        self.assertEquals(0, process.poll())
        os.remove(PATH_TEST_FILE)
        os.chdir('src/tst')
