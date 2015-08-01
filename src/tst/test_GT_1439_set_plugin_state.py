#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')
from db_model import setPluginState, getDbObject

NAME = 'name'
PLUGINS = 'plugins'
TEST_NAME = 'test_1439_set'
ENABLED = 'enabled'
TEST_NEW_NAME = 'test_1439_set_new'

class TestSetPluginState(unittest.TestCase):
    def testSetPluginState(self):
        db = getDbObject()
        db[PLUGINS].save({NAME: TEST_NAME, ENABLED: True})
        setPluginState(TEST_NAME, False)
        obj = db[PLUGINS].find_one({NAME: TEST_NAME})
        self.assertEqual(obj[ENABLED], False)
        setPluginState(TEST_NEW_NAME, True)
        obj = db[PLUGINS].find_one({NAME: TEST_NEW_NAME})
        self.assertEqual(obj[ENABLED], True)