#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
from papache_conf_generator import generate

SAVE_FOLDER = 'config/'
FILE_NAME = 'test'
SERVER_NAME = 'testServerName'
FOLDER = '/var/www/geomongo'
ERROR = "error"


class TestGenerateConfig(unittest.TestCase):
    def testGenerate(self):
        os.chdir('../../')
        # создаю конфиг
        generate(SERVER_NAME, FOLDER, FILE_NAME, ERROR)
        # проверяю создался ли он
        res = os.path.exists(SAVE_FOLDER + FILE_NAME + '.conf')
        os.chdir('src/tst/')
        self.assertEqual(True, res)

