#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import os
import subprocess

PY_SCRIPT = 'python ../../scripts/validate_clone.py --file '
NAME_FILE = 'test_forclonedigger.py'
PATH_TEST_FILE = NAME_FILE
TEXT_PROG_NO_CLONE = 'def fibonacci(max):\n    \
a = 1\n    \
b = 1\n    \
print(a+b)'
TEXT_PROG_WITH_CLONE = 'def fun1(n):\n    \
i = 0\n    \
while i<n:\n        \
if i%2 == 0:\n            \
print i\n    \
i = i + 1\n\n\
def fun2(n):\n    \
i = 0\n    \
while i<n:\n        \
if i%2 != 0:\n            \
print i\n    \
i = i + 1\n'
SRC_W = 'w+'


class TestValidateClone(TestCase):

    def testValidatePlugin_MakeFileWithClone(self):
        file_main = open(NAME_FILE, SRC_W)
        file_main.write(TEXT_PROG_WITH_CLONE)
        file_main.close()
        process = subprocess.Popen(
            PY_SCRIPT + PATH_TEST_FILE,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
        process.communicate()
        self.assertEquals(1, process.poll())
        os.remove(PATH_TEST_FILE)

    def testValidatePlugin_MakeFileNoClone(self):
        file_main = open(NAME_FILE, SRC_W)
        file_main.write(TEXT_PROG_NO_CLONE)
        file_main.close()
        process = subprocess.Popen(
            PY_SCRIPT + PATH_TEST_FILE,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
        process.communicate()
        self.assertEquals(0, process.poll())
        os.remove(PATH_TEST_FILE)
