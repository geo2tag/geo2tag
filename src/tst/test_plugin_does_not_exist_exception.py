#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../')

from plugin_does_not_exist_exception import PluginDoesNotExistException


class TestServiceNotExistException(unittest.TestCase):

    def testServiceNotExistException(self):
        with self.assertRaises(PluginDoesNotExistException) as e:
            raise PluginDoesNotExistException('plugin')
