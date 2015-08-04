#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')
from main import getApi


class TestGetApi(unittest.TestCase):
    def testGetApi(self):
        obj1 = getApi()
        obj2 = getApi()
        self.assertEqual(obj1, obj2)