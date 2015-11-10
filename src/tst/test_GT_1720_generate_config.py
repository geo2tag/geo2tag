#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
from papache_conf_generator import generate

SAVE_FOLDER = 'config/'
FILE_NAME = 'test.conf'
SERVER_NAME = 'testServerName'
FOLDER = 'geomongo'
ERROR = "error"
PORT = 80


class TestGenerateConfig(unittest.TestCase):

    def testGenerate(self):
        os.chdir('../../')
        # create config
        generate(SERVER_NAME, FOLDER, FILE_NAME, ERROR, PORT)
        # check for file exists
        res = os.path.exists(SAVE_FOLDER + FILE_NAME)
        os.chdir('src/tst/')
        self.assertEqual(True, res)
