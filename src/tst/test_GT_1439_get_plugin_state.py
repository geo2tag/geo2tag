#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')
from db_model import getPluginState, getDbObject

NAME = 'name'
PLUGINS = 'plugins'
TEST_NAME = 'test_1439_get'
ENABLED = 'enabled'


class TestGetPluginState(unittest.TestCase):

    def testGetPluginState(self):
        db = getDbObject()
        db[PLUGINS].save({NAME: TEST_NAME, ENABLED: True})
        obj = getPluginState(TEST_NAME)
        self.assertEqual(obj, True)
        obj = getPluginState('aaaaaaa')
        self.assertEqual(obj, False)
